
import eventlet
import socketio
from loguru import logger


ROOMS = ["lobby", "general", "random"]
# Заставляем работать пути к статике
static_files = {'/': 'static/index.html', '/static': './static'}
sio = socketio.Server(cors_allowed_origins='*', async_mode='eventlet')
app = socketio.WSGIApp(sio, static_files=static_files)

# Обрабатываем подключение пользователя
@sio.event
def connect(sid, environ):
    logger.info(f"Пользователь {sid} подключился")

# Обрабатываем запрос очерендного вопроса
@sio.on('get_rooms')
def on_get_rooms(sid, data):
   pass

# Обрабатывем отправку ответа
@sio.on('message')
def on_message(sid, data):
    pass


# Обрабатывем отправку ответа
@sio.on('leave')
def on_leave(sid, data):
    pass


# Обрабатываем отключение пользователя
@sio.event
def disconnect(sid):
     logger.info(f"Пользователь {sid} отключился")


eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 80)), app)
