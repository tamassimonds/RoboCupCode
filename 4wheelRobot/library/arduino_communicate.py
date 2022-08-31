
#!/usr/bin/python3



from os import PRIO_PGRP
from turtle import distance
import serial
import time

import requests
import time
import colors

lastDistance = 0



try:
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout =5)
except:
    try:
        ser = serial.Serial('/dev/ttyACM1', 115200, timeout =5)
    except:
        try:
            ser = serial.Serial('/dev/ttyACM2', 115200, timeout =5)
        except:
            try:
                ser = serial.Serial('/dev/ttyACM3', 115200, timeout =5)
            except:
                try:
                    ser = serial.Serial('/dev/ttyACM4', 115200, timeout =5)
                except:
                    pass

# read from Arduino


input = ""




def parseInput(input, sensorHistory):
    
    #Takes the input from the arduino and parses the strin into its values

    #The format used it
    # D#  for distance sensor, # is the number of the distance sensor 1-3
    # IMU gives the pitch roll and yaw
    arduinoData = input.split("\n")

    for data in arduinoData:
        #print(data)
        if "DS1" in data:
            distanceSensor1 = float(data.split(" ")[1])
            sensorHistory["DS1"].append(distanceSensor1)
        if "DS2" in data:
            distanceSensor2 = float(data.split(" ")[1])
            sensorHistory["DS2"].append(distanceSensor2)
        if "DS3" in data:
            distanceSensor3 = float(data.split(" ")[1])
            sensorHistory["DS3"].append(distanceSensor3)
        if "Pitch" in data:
            sensorHistory["pitch"].append(float(data.split(" ")[1]))
            sensorHistory["roll"].append(float(data.split(" ")[3]))
            sensorHistory["yaw"].append(float(data.split(" ")[5]))

            
 
    return sensorHistory
    
def averageList(lst):
    if len(lst) != 0:
        return sum(lst) / len(lst)
    else:
        return 0

def readArduinoData():
    sensorData = {}
    sensorHistory = {}
    sensorHistory["DS1"] = []
    sensorHistory["DS2"] = []
    sensorHistory["DS3"] = []
    sensorHistory["yaw"] = []
    sensorHistory["roll"] = []
    sensorHistory["pitch"] = []
    
    #Below is some very bad code but it works and its 1am so it will do
    #Good luck debugging this if it doesn't work though

    #the for loop is a bit of a botch but it just reads a few lines before updating the values
    #The issue was the program is single threaded so if we just read one value form the arduino we would them have to wait
    #for the camera program to execture
    #the program is I/O bound so this was a bottle neck

    #Need to add average to smooth noise

    for i in range(10):
       
        if ser.in_waiting > 0:
            try:
                input = ser.readline().decode("utf-8").rstrip()                
            except:
                input = ""
                print(f"{colors.FAIL }ERROR: Unable to read Data from arduino, please check wiring{colors.ENDC}")
            
        
            try:
                if input == "":
                    pass
                else:
                    
                    sensorHistory = parseInput(input, sensorHistory)
            except:
                print("Failed to read sensor data")
        
    #print(sensorHistory)
    
    
    sensorData["DS1"] = averageList(sensorHistory["DS1"])
    sensorData["DS2"] = averageList(sensorHistory["DS2"])
    sensorData["DS3"] = averageList(sensorHistory["DS3"])
    sensorData["pitch"] = averageList(sensorHistory["pitch"])
    sensorData["yaw"] = averageList(sensorHistory["yaw"])
    sensorData["roll"] = averageList(sensorHistory["roll"])

    ser.flushInput()
    return sensorData