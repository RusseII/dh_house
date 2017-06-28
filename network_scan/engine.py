#from scan import findRoommates


class Engine_network_scan():

    def __init__(self):
        print("created engine object")

    def execute(self):
        roomies = findRoommates()
        return roomies.find_roommates()
