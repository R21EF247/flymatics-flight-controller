import math
class drone():
    def __init__(self,r):
        self.rotors=r
        self.thrust=0
        self.rpms=[0 for i in range(r)]
        return None
    def setthrust(self,t):
        self.thrust=t
        self.rpms=[t for i in range(self.rotors)]
        return None
    def moveDirection(self,angle,speed,correction):
        for i in range(self.rotors):
            self.rpms[i]=self.thrust+(correction*self.thrust*speed*math.cos(angle-(i*2*3.1415926535/self.rotors)))
        return None
    def showSpeed(self):
        for i in range(self.rotors):
            print("*"*(int(self.rpms[i]*10)),end="\n")
        print("")
        print(sum(self.rpms))
        return None
a=drone(4)
