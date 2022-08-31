
import colors

import os
import numpy as np
import curses
from curses import wrapper


class Debug():

    D1Value = 0 
    D2Value = 0
    D3Value = 0
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
    
  

     
    

# Display



    def printGreen(self,string):
        print(f"{colors.OKGREEN   } {string}  {  colors.ENDC}")
    def printRed(self,string):
        print(f"{colors.FAIL   } {string}  {  colors.ENDC}")
    def printBlue(self,string):
        print(f"{colors.OKBLUE   } {string}  {  colors.ENDC}")
    def printYellow(self,string):
        print(f"{colors.WARNING   } {string}  {  colors.ENDC}")


    def graph_data(self,D1Value):
        self.timeCount += 1

        
            
        self.plot1.set_xdata(self.x)
        self.plot1.set_ydata(D1Value)
        
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()
        plt.show()

    def printAllSensors(self):
        self.printGreen(f"D1Value: {self.D1Value}\nD2Value: {self.D2Value}\nD3Value:{self.D3Value}\npitch: {self.pitch}\nroll: {self.roll}\nyaw:{self.yaw}\n")

        self.printYellow(f"Center: {self.center}\nRadius:{self.radius}")

    def main(self, stdscr):
        stdscr.clear()
        stdscr.addstr("hello world")
        

        stdscr.refresh()
    #No function should ever be passed this many values 
    def update(self, D1Value, D2Value, D3Value, L1Value, L2Value, L3Value, L4Value, pitch, yaw, roll,center, radius, SCREEN_CONNECTED):
        os.system('cls' if os.name == 'nt' else 'clear')
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
        
        self.printAllSensors()
        
    def __init__(self):
        wrapper(self.main)
    

if __name__ == "__main__":
    debug = Debug()
    debug.update(1,2,3,4,5,6,7,8,9,10,11,13,True)