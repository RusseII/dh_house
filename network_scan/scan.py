import subprocess
import json
import os


class findRoommates():

    def __init__(self):
        print("created findRoommates object")

    def find_roommates(self):
        Roos = "Russell is not home"
        Grace = "Grace is not in my appartment"
        Steve = "Steve is not home"
        Nick = "Nick is not home"
        passw = os.environ['PI_PASS']
        subprocess.call(
            "echo " + passw + " | sudo -S arp-scan --localnet  > allout.txt 2>&1", shell=True)

        if 'e8:8d:28:c5:65:19' in open('allout.txt').read():
            Roos = "Russell is home"

        if '00:a0:c6:eb:5c:6f' in open('allout.txt').read():
            Roos = "Russell is home"

        if 'ac:cf:85:12:42:1d' in open('allout.txt').read():
            Steve = "Steve is home"

        if '6c:72:e7:cf:64:67' in open('allout.txt').read():
            Nick = "Nick is home"
            # 8:31:c1:c5:a9:b0 nicks laptop

        # if '12:b3:b7:d2:e2:3d' in open('allout.txt').read():
        #     Grace = "Grace is at my appartment"

        roommates = [
            {"room": Roos, },
            {"room": Steve, },
            {"room": Nick, },
            {"room": Grace, }
        ]
        roommates = json.dumps(roommates)
        print(roommates)
        return roommates
