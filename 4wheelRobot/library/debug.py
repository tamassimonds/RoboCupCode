
import colors

import os
import numpy as np
import time
import curses
from curses import wrapper

from matplotlib import pyplot as plt


class Debug():

    D1Value = 0 
    D2Value = 0
    D3Value = 0
    D1ValueHistory = []
    D2ValueHistory = []
    D3ValueHistory = []
    L1Value = 0
    L2Value = 0
    L3Value = 0
    L4Value = 0
    pitch = 0
    yaw  = 0
    roll = 0
    center = None
    radius = None
    sensors = []
    x, y = [],[]
    timeCount = 0
    internalCount = 0
    
  

     


# Display



    def printGreen(self,string):
        print(f"{colors.OKGREEN   } {string}  {  colors.ENDC}")
    def printRed(self,string):
        print(f"{colors.FAIL   } {string}  {  colors.ENDC}")
    def printBlue(self,string):
        print(f"{colors.OKBLUE   } {string}  {  colors.ENDC}")
    def printYellow(self,string):
        print(f"{colors.WARNING   } {string}  {  colors.ENDC}")


    def graph_data(self):
        GRAPH_MAX_X = 100
        plt.clf()
        if len(self.D1ValueHistory) > GRAPH_MAX_X+1:
            y1 = self.D1ValueHistory[-GRAPH_MAX_X:]
            x1 = range(len(self.D1ValueHistory[-GRAPH_MAX_X:]))
            y2 = self.D2ValueHistory[-GRAPH_MAX_X:]
            x2 = range(len(self.D2ValueHistory[-GRAPH_MAX_X:]))
            y3 = self.D3ValueHistory[-GRAPH_MAX_X:]
            x3 = range(len(self.D3ValueHistory[-GRAPH_MAX_X:]))
        else:
            y1 = self.D1ValueHistory
            x1 = range(len(self.D1ValueHistory))
            y2 = self.D2ValueHistory
            x2 = range(len(self.D2ValueHistory))
            y3 = self.D3ValueHistory
            x3 = range(len(self.D3ValueHistory))
        
        #print(self.D1ValueHistory)

        plt.scatter(x1, y1, c ="blue", label="D1")
        plt.scatter(x2, y2, c ="green", label="D2")
        plt.scatter(x3, y3, c ="red", label="D3")
        plt.legend(loc="upper left")
        

        plt.ylabel('Sensor Data')
        plt.xlabel('Count(time)')
        
        plt.savefig('sensorData.png')

    def printAllSensors(self):
        self.printGreen(f"D1Value: {self.D1Value}\nD2Value: {self.D2Value}\nD3Value:{self.D3Value}\npitch: {self.pitch}\nroll: {self.roll}\nyaw:{self.yaw}\n")

        self.printYellow(f"Center: {self.center}\nRadius:{self.radius}")
       # time.sleep(0.01)
    
    def updateSensorHistory(self):
        self.D1ValueHistory.append(self.D1Value)
        self.D2ValueHistory.append(self.D2Value)
        self.D3ValueHistory.append(self.D3Value)

    #No function should ever be passed this many values 
    def update(self, D1Value, D2Value, D3Value, L1Value, L2Value, L3Value, L4Value, pitch, yaw, roll,center, radius, SCREEN_CONNECTED):
        #os.system('cls' if os.name == 'nt' else 'clear')
        self.internalCount +=1

        self.sensors =[ D1Value, D2Value, D3Value, L1Value, L2Value, L3Value, L4Value, pitch, yaw, roll,center, radius]
        self.D1Value = D1Value
        self.D2Value = D2Value
        self.D3Value = D3Value
        self.L1Value = L1Value
        self.L2Value = L2Value
        self.L3Value = L3Value
        self.L4Value = L4Value
        self.pitch = pitch
        self.yaw  = yaw
        self.roll = roll
        self.center = center
        self.radius = radius
        self.updateSensorHistory()
        self.printAllSensors()
        
        if self.internalCount%80 == 0:
            self.graph_data()
        
    


if __name__ == "__main__":
    debug = Debug()
    debug.update(1,2,3,4,5,6,7,8,9,10,11,13,True)