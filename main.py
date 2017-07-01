from network_scan.scan import findRoommates
from flask import Flask, flash, request, redirect, url_for, render_template

from flask_socketio import SocketIO, send, emit, join_room, leave_room, \
    Namespace
import threading


from threading import Timer, Thread, Event
from time import sleep
import time

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
    print("visited")
    return all_info.show_who_is_home()

@socketio.on('loaded')
def on_visit():
    socketio.emit('house_occupants_updated', all_info.who_is_home)


def push_event():

    if all_info.is_there_event_and_scan():
        socketio.emit('house_occupants_updated', all_info.who_is_home)

    print(all_info.who_is_home)
    threading.Timer(30, push_event).start()


push_event()


if __name__ == "__main__":
    print("running!")
    socketio.run(app, host="0.0.0.0", port=5000)
