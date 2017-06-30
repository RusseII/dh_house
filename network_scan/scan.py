import subprocess
import json
import os


class findRoommates():

    def __init__(self):
        print("created findRoommates object")
        self.Roos = "False"
        self.Grace = "False"
        self.Steve = "False"
        self.Nick = "False"

        self.roos_counter = 0
        self.steve_counter = 0
        self.nick_counter = 0
        self.passw = os.environ['PI_PASS']
        self.who_is_home = "test"

    def scan_and_counter(self):

        subprocess.call(
            "echo " + self.passw +
            " | sudo -S arp-scan --localnet  > allout.txt 2>&1",
            shell=True)
        counter_celing = 9

        if 'e8:8d:28:c5:65:19' in open('allout.txt').read():
            if self.roos_counter < counter_celing:
                self.roos_counter += counter_celing
                self.Roos = "True"
        else:
            if self.roos_counter > 0:
                self.roos_counter -= 1

        if 'ac:cf:85:12:42:1d' in open('allout.txt').read():
            if self.steve_counter < counter_celing:
                self.steve_counter += counter_celing
                self.Steve = "True"
        else:
            if self.steve_counter > 0:
                self.steve_counter -= 1

        if '6c:72:e7:cf:64:67' in open('allout.txt').read():
            if self.nick_counter < counter_celing:
                self.nick_counter += counter_celing
                self.Nick = "True"
        else:
            if self.nick_counter > 0:
                self.nick_counter -= 1

        if self.nick_counter == 0:
            self.Nick = "False"
        if self.roos_counter == 0:
            self.Roos = "False"
        if self.steve_counter == 0:
            self.Steve = "False"
        return "DONE"

        # 8:31:c1:c5:a9:b0 nicks laptop

        # if '12:b3:b7:d2:e2:3d' in open('allout.txt').read():
        #     Grace = "Grace is at my appartment"

        # roommates = [
        #     {"room": Roos, },
        #     {"room": Steve, },
        #     {"room": Nick, },
        #     {"room": Grace, }
        # ]
        # roommates = json.dumps(roommates)
        # print(roommates)
        # return roommates

    def show_who_is_home(self):
        self.who_is_home = [{
            "Roos": self.Roos,
        }, {
            "Steve": self.Steve,
        }, {
            "Nick": self.Nick,
        }, {
            "Grace": self.Grace,
        }]
        # names = json.dumps(self.who_is_home)

        # return names

    def is_there_event_and_scan(self):
        self.scan_and_counter()
        # print(json.dumps(self.who_is_home))

        l = [{
            "Roos": self.Roos,
        }, {
            "Steve": self.Steve,
        }, {
            "Nick": self.Nick,
        }, {
            "Grace": self.Grace,
        }]

        if (self.who_is_home == l):
            return False
        else:
            self.who_is_home = l
            return True


if __name__ == '__main__':
    test = findRoommates()
    for i in range(20000):
        print(test.is_there_event_and_scan())
        print(test.show_who_is_home())
