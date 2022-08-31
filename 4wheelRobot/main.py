


#Debug Settings
PRINT_SENSOR_DATA = True 
USING_PICAMERA = True
CAMERA_SHOW_PREVIEW = True

last_move = ""


DEBUG_MODE = True



if __name__ == "__main__":
    print("SETTTING UP")

import time

import controller
import os, sys
sys.path.insert(0,'library')# insert the folder lib in system path
import motor_controller as mc
import math

if DEBUG_MODE:
    import debug

#Values from your arduiono


CAMERA_WIDTH = 600
CAMERA_HEIGHT = int(600/(1.33))


ANGLE_OFFSET = 37 #OFFET OF CAMERA AND MIRROR 
#Put ball infront and measure angle to find offset



#LS1 right
#LS2 Forward
#LS3 LEFT
#LS4 back


debugClass = debug.Debug()
def mainLoop():
    count = 0
    controller.setup(USING_PICAMERA, CAMERA_SHOW_PREVIEW)
    while True:
        controller.update()
        (D1Value, D2Value, D3Value, L1Value, L2Value, L3Value, L4Value, pitch, yaw, roll) = controller.getArduinoValues()
        #print("test")
        center, radius = controller.getBallPosCamera()
        #CAMERA x between 0 and 300
        #Camera y between 
        
        if center != None:
            if CAMERA_WIDTH/2 - center[0] != 0:
                angle = math.degrees((math.atan((CAMERA_HEIGHT/2 - center[1])/ (CAMERA_WIDTH/2 - center[0])))) - ANGLE_OFFSET
            radius = math.sqrt((CAMERA_HEIGHT/2 - center[1])**2 + (CAMERA_WIDTH/2 - center[0])**2 ) 
        
            ballPrintString = f"BALL: center {center} angle {angle} radius {radius}" 
            controller.printYellow(ballPrintString)

        if DEBUG_MODE:
            debugClass.update( D1Value, D2Value, D3Value, L1Value, L2Value, L3Value, L4Value, pitch, yaw, roll, center, radius, CAMERA_SHOW_PREVIEW)


        # count +=1
        # print(count)
        # if count > 100:
        #     mc.move_backwards()
        # elif count > 200:
        #     mc.stop_all()
        #     count = 0 

        


        #controller.followBall(center, radius)

        #print(D1Value, D2Value, D3Value, yaw, roll, pitch ,center, radius)
        
        #print(D1Value)
        
        # (blueGoalCenter, blueGoalRadius) = controller.detectBlueGoal()
        
        # print(L1Value, L2Value, L3Value, L4Value)

        
        
        # (yellowGoalCenter, yellowGoalRadius) = controller.detectYellowGoal()
        # print("Blue Goals", blueGoalCenter, blueGoalRadius , "Yellow Goals", yellowGoalCenter, yellowGoalRadius)

        # print("Blue Goals", blueGoalCenter, blueGoalRadius , "Yellow Goals", yellowGoalCenter, yellowGoalRadius)
        
        



if __name__ == "__main__":
    print("CONFIGURATION COMPLETE")
    
    mainLoop()




