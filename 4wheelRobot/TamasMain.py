

if __name__ == "__main__":
    print("SETTTING UP")

import time
from datetime import datetime
import controller
import os, sys
sys.path.insert(0,'library')# insert the folder lib in system path
import motor_controller as mc


#Values from your arduiono


#Debug Settings
PRINT_SENSOR_DATA = False 
USING_PICAMERA = True
CAMERA_SHOW_PREVIEW = False

last_move = ""


#D2 is right
#D3 is back
#D1 is left

def mainLoop():
    controller.setup(USING_PICAMERA, CAMERA_SHOW_PREVIEW)
    
    # mc.move_right()
    # time.sleep(1)
    # mc.stop_all()
    # mc.move_left()
    # time.sleep(1)
    # mc.stop_all()

 
    lastD2Value = 500
    while True:
        
        controller.update()
        (D1Value, D2Value, D3Value, pitch, yaw, roll) = controller.getArduinoValues()
        #print("test")
        center, radius = controller.getBallPosCamera()
        #CAMERA x between 0 and 300
        #Camera y between 
        if PRINT_SENSOR_DATA:
            controller.printAllSensorData(D1Value, D2Value, D3Value, yaw, roll, pitch ,center, radius)
        
        # (leftPost, rightPost) = controller.detectBlueGoal()
        
        # print("Blue POSTS", leftPost, rightPost)
        # (leftPost, rightPost) = controller.detectYellowGoal()
        # print("Yellow POSTS", leftPost, rightPost)
        print("center",center)
        
        if center != None:
                
                if radius > 35:
                    
                    #THis means the ball is really close
                   # mc.move_forward()
                   pass
                else:
                    if center[0] < 100:
                        mc.move_left()
                    elif center[0] > 200:
                        mc.move_right()
                    else:
                        mc.stop_all()
        else:
            #this means the robot does not see the ball
            if yaw < -20:
                mc.rotate_left(50)
                print("ROTATING LEFT")
            elif yaw > 20:
                print("ROTATING RIGHT") 
                mc.rotate_right(50)
            else:
                print("FACING FORWARD")
                mc.stop_all()
            pass

        #TURN TO FACE FORWARD
        # 
        
            

        # if D2Value > D1Value - 10:
        #     mc.move_right()
        # elif D1Value > D2Value - 10:
        #     mc.move_left()
        # else:

        #     print("Center")
        #     mc.stop_all()
        #    # break
        
        
        
     












        #To do list
        #find a way to see if ball in opposite half
        #Find a w way to find the center of the pitch
        #Move to center of the pitch
        
        #Attack
        #move to edge
        #Color sensor and Distance sensor


        #Defence
        #Go back to edge goal line
        #Find edge of goal
        #


        #Go Lefts if ball to left
        #Drives right if ball to right
        #Drives forward if ball infront and close

        # center[0] #x coordiante 0 and 300 
        # #150 is center
        # center[1] #y coordinate
        # robotInBox = False

        # #Goalie
        # if center != None:
        #     #means we can see the ball
        #     if robotInBox:
        #         if center[0] < 130:
        #             #The balls is to the left
        #             #drive to left
        #             mc.move_left()
        #         elif center[0] > 170:
        #             #The ball is to the right
        #             mc.move_right()
                    
        #         else:
                
        #             mc.motor1_forward()
        #     else:
        #         #write some code to get back in the box
        #         pass
        # else:
        #     #if we can't see the ball
        #     pass

        # #Attacker
        # #Boal is in then half
        # #360 camera here
        # #we can see goals and the ball
        
        # #Chase ball if its in there half
        # #Don't drive outside white lines
        
        # #Write code to figure this out
        # ballInThereHalf = True

        # if ballInThereHalf:
        #     #Attacking stuff
        #     #Drive towards the ball
            
        #     #we can't see the ball
        #     #What happends if we are facing another robot
        #     #How do we not go out of bounds
            
        #     #How do we use the kicker

        #     #how do we direct the ball towards the goal

        #     #attacker between the ball and our goal

        #     if center != None:
        #         if center[0] < 130:
        #             #The balls is to the left
        #             #drive to left
        #             mc.move_left()
        #         elif center[0] > 170:
        #             #The ball is to the right
        #             mc.move_right()   
        #         else:
        #             mc.motor1_forward()
        #     else:
        #         #search for the ball for 3 seconds
        #         #then go back to goal
        #         #Go to the middle
                
        #         pass
                
        # else:
        #     #Defending stuff
        #     pass
            



        # #Compass
        # #0 degree is opposition goal


        #     #Means we can not see the ball




      


                





if __name__ == "__main__":
    print("CONFIGURATION COMPLETE")
    
    mainLoop()




