from network_scan.engine import Engine_network_scan
from network_scan.scan import findRoommates
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
# import subprocess
# import json

app = Flask(__name__)

# resume
all_info = findRoommates()


# roomate network_scan
@app.route('/', methods=['GET', 'POST'])
def roommates():
    return render_template("roommates.html")


@app.route('/scan', methods=['GET'])
def ping_who_is_here():
    all_info.show_who_is_home()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
