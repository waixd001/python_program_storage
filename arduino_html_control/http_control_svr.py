from threading import Lock
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, \
close_room, rooms, disconnect

async_mode = None

app = Flask(__name__)

app.config['KEY'] = 'HAHA'
socketio = SocketIO(app, async_mode=async_mode)

thread = None
thread_lock = Lock()

def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        socketio.sleep(10)
        count += 1
        print("EMIT")
        socketio.emit('my_response',
                      {'data': 'Server generated event', 'count': count})

@app.route('/')
def index():
	return render_template('index.html')
	
@socketio.on( 'mode changer')
def event (txt):
	print(txt)
	if (txt == "data"):
		print("Fuck yea")
	mode = '已開啟'
	socketio.emit('update', { 'item': txt, 'now': mode})

@socketio.on('connect')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)
    emit('my_response', {'data': 'Connected', 'count': 0})

if __name__ == '__main__':
	socketio.run(app,debug = True )

