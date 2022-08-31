#Controller interfaces with the library for students

import time
import os, shutil, sys

sys.path.insert(0,'library')# insert the folder lib in system path
import arduino_communicate 
import motor_controller as mc
import cameraDetection
import colors

CAMERA_SHOW_PREVIEW = None

def setup(USING_PICAMERA, CAMERA_SHOW_PREVIEW_Passed):
    global CAMERA_SHOW_PREVIEW

    #Deletes old saved camera preview images and replaces with new
    shutil.rmtree('detectedImage')
    os.mkdir("detectedImage")

    if USING_PICAMERA:
        cameraDetection.setupCamera()
        CAMERA_SHOW_PREVIEW = CAMERA_SHOW_PREVIEW_Passed

WIDTH = 300

BALLINFRONTRANGE = WIDTH/4

arduinoSensorData = {"DS1": 0, "DS2": 0, "DS3": 0, "LS1":0, "LS2":0,"LS3":0,"LS4":0, "pitch": 0, "yaw":0, "roll": 0}

def updateMainArduinoVariables(dataFromArduiono):
    #Updates the variables in the main file
    if "DS1" in dataFromArduiono:
        arduinoSensorData["DS1"] = dataFromArduiono["DS1"]
    if "DS2" in dataFromArduiono:
        arduinoSensorData["DS2"] = dataFromArduiono["DS2"]
    if "DS3" in dataFromArduiono: 
        arduinoSensorData["DS3"] = dataFromArduiono["DS3"]
    if "LS1" in dataFromArduiono:
        arduinoSensorData["LS1"] = dataFromArduiono["LS1"]
    if "LS2" in dataFromArduiono:
        arduinoSensorData["LS2"] = dataFromArduiono["LS2"]
    if "LS3" in dataFromArduiono: 
        arduinoSensorData["LS3"] = dataFromArduiono["LS3"]
    if "LS4" in dataFromArduiono: 
        arduinoSensorData["LS4"] = dataFromArduiono["LS4"]
    if "yaw" in dataFromArduiono: 
        arduinoSensorData["yaw"] = dataFromArduiono["yaw"]
    if "pitch" in dataFromArduiono: 
        arduinoSensorData["pitch"] = dataFromArduiono["pitch"]
    if "roll" in dataFromArduiono: 
        arduinoSensorData["roll"] = dataFromArduiono["roll"]
    
def update():
    pass

def getArduinoValues():
    dataFromArduiono = arduino_communicate.readArduinoData()
    
    if dataFromArduiono != None:
        updateMainArduinoVariables(dataFromArduiono)
    
    return arduinoSensorData.values()

def getBallPosCamera():
    (center, radius) = cameraDetection.detectBall(CAMERA_SHOW_PREVIEW)
    return (center, radius)

def detectYellowGoal():
    (leftPost, rightPost) = cameraDetection.detectYellowGoal()
    return (leftPost, rightPost)
def detectBlueGoal():
    #returns pos of left and right post x cord
    (leftPost, rightPost) = cameraDetection.detectBlueGoal()
    return (leftPost, rightPost)

def printAllSensorData(D1Value, D2Value, D3Value, yaw, roll, pitch ,center, radius):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{colors.OKGREEN   } D1Value: {D1Value} D2Value: {D2Value} D3Value: {D3Value} pitch: {pitch} roll: {roll} yaw: {yaw} center: {center} radius: {radius}  {  colors.ENDC}")

def printGreen(string):
    print(f"{colors.OKGREEN   } {string}  {  colors.ENDC}")
def printRed(string):
    print(f"{colors.FAIL   } {string}  {  colors.ENDC}")
def printBlue(string):
    print(f"{colors.OKBLUE   } {string}  {  colors.ENDC}")
def printYellow(string):
    print(f"{colors.WARNING   } {string}  {  colors.ENDC}")
