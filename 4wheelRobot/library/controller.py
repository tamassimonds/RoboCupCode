#Controller interfaces with the library for students

import time
import os, sys

sys.path.insert(0,'library')# insert the folder lib in system path
import arduino_communicate 
import motor_controller as mc
import cameraDetection
import colors

CAMERA_SHOW_PREVIEW = None

def setup(USING_PICAMERA, CAMERA_SHOW_PREVIEW_Passed):
    global CAMERA_SHOW_PREVIEW
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
    print(f"{colors.OKGREEN   } D1Value: {D1Value} D2Value: {D2Value} D3Value: {D3Value} pitch: {pitch} roll: {roll} yaw: {yaw} center: {center} radius: {radius}  {  colors.ENDC}")

def printGreen(string):
    print(f"{colors.OKGREEN   } {string}  {  colors.ENDC}")
def printRed(string):
    print(f"{colors.FAIL   } {string}  {  colors.ENDC}")
def printBlue(string):
    print(f"{colors.OKBLUE   } {string}  {  colors.ENDC}")
def printYellow(string):
    print(f"{colors.WARNING   } {string}  {  colors.ENDC}")


def followBall(center, radius):
    global last_move
    if radius != None and radius > 0:
        if center[0] > WIDTH/2 + BALLINFRONTRANGE:
            print("left")
            if last_move != "left":
                mc.stop_all()
                #time.sleep(0.03)
            mc.motor1_forward()
            mc.motor2_forward()
            mc.motor3_forward()
            time.sleep(0.01)
            mc.stop_all()
            last_move = "left"
        elif center[0] < WIDTH/2 - BALLINFRONTRANGE:
            print("right")
            if last_move != "right":
                mc.stop_all()
               # time.sleep(0.03)
            mc.motor1_backward()
            mc.motor2_backward()
            mc.motor3_backward()
            time.sleep(0.01)
            mc.stop_all()
            last_move = "right"
        else:
            print("forward")
            if last_move != "forward":
                mc.stop_all()
               # time.sleep(0.3)
            mc.motor3_forward()
            mc.motor2_backward()
            time.sleep(0.1)
            
            last_move = "forward"

        if radius > 80:
            print("forward")
            mc.stop_all()
            mc.motor3_forward()
            mc.motor2_backward()

    else:
        print("Ball not found, searching for ball")
        #this means that there was no ball found
        #Should probably stop motors
        mc.stop_all()
        mc.motor1_backward()
        mc.motor2_backward()
        mc.motor3_backward()
        time.sleep(0.01)
        mc.stop_all()
        #mc.motor1_forward()
