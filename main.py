import eventlet
from eventlet import wsgi
import socketio
from loguru import logger

from src.models.user import User
from src.models.message import Message

ROOMS = ["lobby", "general", "random"]

# Заставляем работать пути к статике
static_files = {'/': 'static/index.html', '/static': './static'}
sio = socketio.Server(cors_allowed_origins='*', async_mode='eventlet')
app = socketio.WSGIApp(sio, static_files=static_files)


# Обрабатываем подключение пользователя
@sio.event
def connect(sid, environ):
    logger.info(f"Пользователь {sid} подключился")


# Отправляем комнаты
@sio.on('get_rooms')
def on_get_rooms(sid, data):
    ...


@sio.on('join')
def on_join(sid, data):
    ...


@sio.on('leave')
def on_leave(sid, data):
    ...


# Обрабатываем отправку ответа
@sio.on('send_message')
def on_message(sid, data):
    ...


# Обрабатываем отключение пользователя
@sio.event
def disconnect(sid):
    logger.info(f"Пользователь {sid} отключился")


if __name__ == '__main__':
    wsgi.server(eventlet.listen(("127.0.0.1", 8000)), app)
