#Interfaces with motors
import argparse
#import pyrebase
import time
import RPi.GPIO as GPIO
import threading

Motor1A = 37  #Left F
Motor1B = 36
Motor2A = 16  #Right F
Motor2B = 18
Motor3A = 33  #Left B
Motor3B = 35
Motor4A = 22  #Right B
Motor4B = 15
KickerA = 38
KickerB = 40


GPIO.cleanup()


GPIO.setmode(GPIO.BOARD)
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor3A,GPIO.OUT)
GPIO.setup(Motor3B,GPIO.OUT)
GPIO.setup(Motor4A,GPIO.OUT)
GPIO.setup(Motor4B,GPIO.OUT)
GPIO.setup(KickerA,GPIO.OUT)
GPIO.setup(KickerB,GPIO.OUT)
fPWM = 100  # Hz (not higher with software PWM)



pwmMotor1A = GPIO.PWM(Motor1A, fPWM)
pwmMotor1A.start(0)
pwmMotor1B = GPIO.PWM(Motor1B, fPWM)
pwmMotor1B.start(0)
pwmMotor2A = GPIO.PWM(Motor2A, fPWM)
pwmMotor2A.start(0)
pwmMotor2B = GPIO.PWM(Motor2B, fPWM)
pwmMotor2B.start(0)
pwmMotor3A = GPIO.PWM(Motor3A, fPWM)
pwmMotor3A.start(0)
pwmMotor3B = GPIO.PWM(Motor3B, fPWM)
pwmMotor3B.start(0)
pwmMotor4A = GPIO.PWM(Motor4A, fPWM)
pwmMotor4A.start(0)
pwmMotor4B = GPIO.PWM(Motor4B, fPWM)
pwmMotor4B.start(0)

pwmKickerA = GPIO.PWM(KickerA, fPWM)
pwmKickerA.start(0)
pwmKickerB = GPIO.PWM(KickerB, fPWM)
pwmKickerB.start(0)


def set_motor1_speed(speed):
    

    if speed > 0:
        motor1_forward(speed)
    elif speed < 0:
        motor1_backward(abs(speed))
    elif speed == 0:
        motor1_stop()
    else:
        print("ERROR Not valid speed input, only accept -100,0,100 and" + str(speed) + "returned")

def set_motor2_speed(speed):

    if speed > 0:
        motor2_forward(speed)
    elif speed < 0:
        motor2_backward(abs(speed))
    elif speed == 0:
        motor2_stop()
    else:
        print("ERROR Not valid speed input, only accept -100,0,100 and" + str(speed) + "returned")

def set_motor3_speed(speed):

    if speed > 0:
        motor3_forward(speed)
    elif speed < 0:
        motor3_backward(abs(speed))
    elif speed == 0:
        motor3_stop()
    else:
        print("ERROR Not valid speed input, only accept -100,0,100 and" + str(speed) + "returned")

def set_motor4_speed(speed):

    if speed > 0:
        motor4_forward(speed)
    elif speed < 0:
        motor4_backward(abs(speed))
    elif speed == 0:
        motor4_stop()
    else:
        print("ERROR Not valid speed input, only accept -100,0,100 and" + str(speed) + "returned")
    

 
def motor1_forward(speed=100):
    pwmMotor1A.ChangeDutyCycle(0)
    pwmMotor1B.ChangeDutyCycle(speed)
    
def motor1_backward(speed=100):
    pwmMotor1A.ChangeDutyCycle(speed)
    pwmMotor1B.ChangeDutyCycle(0)


def motor1_stop():
    pwmMotor1B.ChangeDutyCycle(0)
    pwmMotor1A.ChangeDutyCycle(0)


def motor2_forward(speed=100):
    pwmMotor2A.ChangeDutyCycle(0)
    pwmMotor2B.ChangeDutyCycle(speed)
    
def motor2_backward(speed=100):
    pwmMotor2A.ChangeDutyCycle(speed)
    pwmMotor2B.ChangeDutyCycle(0)
    

def motor2_stop():
    pwmMotor2B.ChangeDutyCycle(0)
    pwmMotor2A.ChangeDutyCycle(0)

def motor3_forward(speed=100):
    pwmMotor3A.ChangeDutyCycle(0)
    pwmMotor3B.ChangeDutyCycle(speed)
    
def motor3_backward(speed=100):
    pwmMotor3A.ChangeDutyCycle(speed)
    pwmMotor3B.ChangeDutyCycle(0)
    

def motor3_stop():
    pwmMotor3B.ChangeDutyCycle(0)
    pwmMotor3A.ChangeDutyCycle(0)

def motor4_forward(speed=100):
    pwmMotor4A.ChangeDutyCycle(0)
    pwmMotor4B.ChangeDutyCycle(speed)
    
def motor4_backward(speed=100):
    pwmMotor4A.ChangeDutyCycle(speed)
    pwmMotor4B.ChangeDutyCycle(0)
    

def motor4_stop():
    pwmMotor4B.ChangeDutyCycle(0)
    pwmMotor4A.ChangeDutyCycle(0)

def stop_all():
    motor1_stop()
    motor2_stop()
    motor3_stop()
    motor4_stop()
    
def move_backwards():
    set_motor1_speed(100)
    set_motor2_speed(100)
    set_motor3_speed(100)
    set_motor4_speed(100)

def move_forward():
    set_motor1_speed(-100)
    set_motor2_speed(-100)
    set_motor3_speed(-100)
    set_motor4_speed(-100)

def move_forward_right():
    set_motor1_speed(-100)
    set_motor2_speed(100)
    set_motor3_speed(75)
    set_motor4_speed(-75)

def move_right():
    set_motor1_speed(-100)
    set_motor2_speed(100)
    set_motor3_speed(75)
    set_motor4_speed(-75)

def move_forward_left():
    set_motor1_speed(100)
    set_motor2_speed(-100)
    set_motor3_speed(-100)
    set_motor4_speed(100)

def move_left():
    set_motor1_speed(100)
    set_motor2_speed(-100)
    set_motor3_speed(-75)
    set_motor4_speed(75)

def rotate_right(speed=100):
    set_motor1_speed(-speed)
    set_motor2_speed(speed)
    set_motor3_speed(-speed)
    set_motor4_speed(speed)

def rotate_left(speed=100):
    set_motor1_speed(speed)
    set_motor2_speed(-speed)
    set_motor3_speed(speed)
    set_motor4_speed(-speed)


def turn_kicker_off():
    print("THREAD DISPATCHED")
    pwmKickerB.ChangeDutyCycle(0)



def kick_on():
    pwmKickerB.ChangeDutyCycle(100)
    t = threading.Timer(0.1, turn_kicker_off)
    t.start()



stop_all()



#Back Right always on
# Front right doesn't go backwards

#Black is on

#move_left()



stop_all()
