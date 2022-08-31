import imp

import keyboard
loop = ""
import sys
count = 0
sys.path.insert(0,'library')
import motor_controller as mc 
keysPressed = {"w": False, "a": False, "s": False, "d": False,"q": False,"e": False, "space": False }


while True:
    if keyboard.is_pressed("space"):
        print("space pressed")
        
        if keysPressed["space"] == False:
            mc.kick_on()
        keysPressed["space"] = True
    else:
        if keysPressed["space"] == True:
            keysPressed["space"] = False
            print("space released")
            mc.stop_all()
    if keyboard.is_pressed("w"):
        #W Pressed
        #if keysPressed["w"] == False:
        keysPressed["w"] = True
        print("You pressed w")
        mc.move_forward()
    
            
    
    else:
        #W Released
        if keysPressed["w"] == True:
            keysPressed["w"] = False
            print("w released")
            mc.stop_all()

    
    if keyboard.is_pressed("a"):
        #a Pressed
        if keysPressed["a"] == False:
            keysPressed["a"] = True
            print("You pressed a")
        mc.move_left()
    else:
        if keysPressed["a"] == True:
            keysPressed["a"] = False
            print("a released")
            mc.stop_all()
    

    if keyboard.is_pressed("s"):
        #s Pressed
        if keysPressed["s"] == False:
            keysPressed["s"] = True
            print("You pressed s")
        mc.move_backwards()
    else:
        #s Released
        if keysPressed["s"] == True:
            keysPressed["s"] = False
            print("s released")
            mc.stop_all()

    if keyboard.is_pressed("d"):
        #d Pressed
        if keysPressed["d"] == False:
            keysPressed["d"] = True
            print("You pressed d")
        mc.move_right()
    else:
        #d Released
        if keysPressed["d"] == True:
            keysPressed["d"] = False
            print("d released")
            mc.stop_all()
    
    

    
    
    if keyboard.is_pressed("q"):
        #q Pressed
        if keysPressed["q"] == False:
            keysPressed["q"] = True
            print("You pressed q")
        mc.rotate_left()
        
            

    else:
        #q Released
        if keysPressed["q"] == True:
            keysPressed["q"] = False
            print("q released")
            mc.stop_all()
    
    if keyboard.is_pressed("e"):
        #e Pressed
        if keysPressed["e"] == False:
            keysPressed["e"] = True
            print("You pressed e")
        mc.rotate_right()
            

    else:
        #e Released
        if keysPressed["e"] == True:
            keysPressed["e"] = False
            print("e released")
            mc.stop_all()