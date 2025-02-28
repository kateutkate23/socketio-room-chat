import eventlet
from eventlet import wsgi
import socketio
from loguru import logger
from pydantic import ValidationError

from src.models.user import User
from src.models.message import Message

ROOMS = ["lobby", "general", "random"]
USERS = {}

# Заставляем работать пути к статике
static_files = {'/': 'static/index.html', '/static': './static'}
sio = socketio.Server(cors_allowed_origins='*', async_mode='eventlet')
app = socketio.WSGIApp(sio, static_files=static_files)


# Обрабатываем подключение пользователя
@sio.event
def connect(sid, environ):
    logger.info(f"Пользователь {sid} подключился")
    USERS[sid] = {}


# Отправляем комнаты
@sio.on('get_rooms')
def on_get_rooms(sid, data):
    sio.emit('rooms', data=ROOMS, to=sid)


@sio.on('join')
def on_join(sid, data):
    try:
        user = User(**data)
        USERS[sid] = user.model_dump()
    except ValidationError as e:
        sio.emit('error', data=e.json(), to=sid)
        return

    sio.save_session(sid, user.model_dump())
    sio.enter_room(sid, data['room'])
    sio.emit('move', data={'room': data['room']}, to=sid)


@sio.on('leave')
def on_leave(sid, data):
    if sid in USERS and 'room' in USERS[sid]:
        sio.leave_room(sid, USERS[sid]['room'])

        session = sio.get_session(sid)
        if session:
            session['room'] = None
            sio.save_session(sid, session)


# Обрабатываем отправку ответа
@sio.on('send_message')
def on_message(sid, data):
    try:
        session = sio.get_session(sid)
        if not session or 'room' not in session or not session['room']:
            sio.emit('error', data={'message': 'You must join the room first'}, to=sid)
            return

        message = Message(text=data['text'], author=session['name'])

        if sid in USERS:
            USERS[sid]['messages'].append(message.model_dump())

        sio.emit('message', data={'name': session['name'], 'text': message.text}, room=session['room'])

    except ValidationError as e:
        sio.emit('error', data=e.json(), to=sid)
    except KeyError as e:
        sio.emit('error', data={'message': f'Missing required field: {str(e)}'}, to=sid)


# Обрабатываем отключение пользователя
@sio.event
def disconnect(sid):
    if sid in USERS and 'room' in USERS[sid]:
        sio.leave_room(sid, USERS[sid]['room'])
    del USERS[sid]

    logger.info(f"Пользователь {sid} отключился")


if __name__ == '__main__':
    wsgi.server(eventlet.listen(("127.0.0.1", 8000)), app)
