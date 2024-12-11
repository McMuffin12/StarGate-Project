#this class will contain everything needed to represent a stargate
class stargate:
    def __init__(self, pos, address, galix):
        self.pos = pos
        self.address = address
        self.galix = galix
        self.connectStatus = False
        self.connectedTo

    # this will return true if this gate is able to make a connection to the dialing gate
    def makeConnection(self):
        pass

    # This will prompt the network to lookup and try and make a connection with the target gate.
    def dial (self):
        pass