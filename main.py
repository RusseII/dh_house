from network_scan.engine import Engine_network_scan
from network_scan.scan import findRoommates
from flask import Flask, flash, request, redirect, url_for, render_template

from flask_socketio import SocketIO, send, emit, join_room, leave_room, \
    Namespace

async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
# resume
all_info = findRoommates()


# roomate network_scan
@app.route('/', methods=['GET', 'POST'])
def roommates():
    return render_template("roommates.html")


@app.route('/scan', methods=['GET'])
def ping_who_is_here():
    all_info.scan_and_counter()
    push_event()
    return all_info.show_who_is_home()


def push_event():
	socketio.emit('house_occupants_updated', all_info.who_is_home)
	print(all_info.who_is_home)



if __name__ == "__main__":
    print("running!")
    socketio.run(app, host="0.0.0.0", port=5000)
