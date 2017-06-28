import subprocess
import json
import os
import time


class findRoommates():

    def __init__(self):
        print("created findRoommates object")
        self.Roos = "Russell is not home"
        self.Grace = "Grace is not in my appartment"
        self.Steve = "Steve is not home"
        self.Nick = "Nick is not home"
        self.roos_counter = 0
        self.steve_counter = 0
        self.nick_counter = 0
        self.passw = os.environ['PI_PASS']
        self.who_is_home = [
                {"room": self.Roos, },
                {"room": self.Steve, },
                {"room": self.Nick, },
                {"room": self.Grace, }
            ]


    def scan_and_counter(self):
        


        subprocess.call(
            "echo " + self.passw + " | sudo -S arp-scan --localnet  > allout.txt 2>&1", shell=True)
        counter_celing = 9

        if 'e8:8d:28:c5:65:19' in open('allout.txt').read():
            if self.roos_counter < counter_celing:
                self.roos_counter += counter_celing
                print("WW")
                self.Roos = "Russell is home"
        else:
            if self.roos_counter > 0:
                self.roos_counter -= 1
          


        if '78:4f:43:4e:5f:67' in open('allout.txt').read():
            if self.steve_counter < counter_celing:
                self.steve_counter += counter_celing
                self.Steve = "Steve is home"
        else:
            if self.steve_counter > 0:
                self.steve_counter -= 1

        if '6c:72:e7:cf:64:67' in open('allout.txt').read():
            if self.nick_counter < counter_celing:
                self.nick_counter += counter_celing
                self.Nick = "Nick is home"
        else:
            if self.nick_counter > 0:
                self.nick_counter -= 1

        if self.nick_counter == 0:
            self.Nick = "Nick is NOT home"
        if self.roos_counter == 0:
            self.Roos = "Roos is NOT home"
        if self.steve_counter == 0:
            self.Steve = "Steve is NOT home"
                
                # 8:31:c1:c5:a9:b0 nicks laptop

            # if '12:b3:b7:d2:e2:3d' in open('allout.txt').read():
            #     Grace = "Grace is at my appartment"

            # roommates = [
            #     {"room": Roos, },
            #     {"room": Steve, },
            #     {"room": Nick, },
            #     {"room": Grace, }
            #]
            # roommates = json.dumps(roommates)
            # print(roommates)
            # return roommates

    def show_who_is_home(self):
        self.who_is_home = [
                {"room": self.Roos, },
                {"room": self.Steve, },
                {"room": self.Nick, },
                {"room": self.Grace, }
            ]
        print (self.nick_counter)
        return self.who_is_home
        names =json.dumps(self.who_is_home)

        return names

    def is_there_event_and_scan(self):
        self.scan_and_counter()
        if (self.who_is_home == [
                {"room": self.Roos, },
                {"room": self.Steve, },
                {"room": self.Nick, },
                {"room": self.Grace, }
            ]):
            return False
        else:
            return True



if __name__ == '__main__':
    test = findRoommates()
    for i in range(20):
        print(test.is_there_event_and_scan())       
        print(test.show_who_is_home())
