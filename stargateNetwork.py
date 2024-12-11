# inport other needed classes


# This class handles all of the stargate interactions and store the locations of the stargates
class stargateNetwork:
    def __init__(self):
        self.gates = list

    def generateAddress(self, location):
        # Local var
        address = ""
        for i in location:
            address += chr(ord("A") + int(i))
        return address
    
    

test = stargateNetwork()
print (test.generateAddress("55555511"))    

    