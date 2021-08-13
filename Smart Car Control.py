import RPi.GPIO as GPIO          
from time import sleep

# Variables

# Wheels

# Left Wheel
in1 = 23
in2 = 24
ena = 25

# Right Wheel
in3 = 5
in4 = 6
enb = 13

# Camera

# Left-Right
in11 = 14
in22 = 15
enaa = 16

# Up-Down
in33 = 20
in44 = 21
enbb = 19

# Setup

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
GPIO.setup(in11,GPIO.OUT)
GPIO.setup(in22,GPIO.OUT)
GPIO.setup(in33,GPIO.OUT)
GPIO.setup(in44,GPIO.OUT)
GPIO.setup(enaa,GPIO.OUT)
GPIO.setup(enbb,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
GPIO.output(in11,GPIO.LOW)
GPIO.output(in22,GPIO.LOW)
GPIO.output(in33,GPIO.LOW)
GPIO.output(in44,GPIO.LOW)
p=GPIO.PWM(ena,1000)
q=GPIO.PWM(enb,1000)
pp=GPIO.PWM(enaa,1000)
qq=GPIO.PWM(enbb,1000)

# Start
p.start(100) ## Left Wheel
q.start(100) ## Right Wheel
pp.start(100) ##LR
qq.start(100) ##UD

# Functions

# Stop
def stop():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(in11,GPIO.LOW)
    GPIO.output(in22,GPIO.LOW)
    GPIO.output(in33,GPIO.LOW)
    GPIO.output(in44,GPIO.LOW)
    print("stop")

# Speeds (Only used for wheels)

def low():
    p.ChangeDutyCycle(25)
    q.ChangeDutyCycle(25)
    print('low')

def medium():
    p.ChangeDutyCycle(50)
    q.ChangeDutyCycle(50)
    print('medium')

def high():
    p.ChangeDutyCycle(75)
    q.ChangeDutyCycle(75)
    print('high')

def maximum():
    p.ChangeDutyCycle(100)
    q.ChangeDutyCycle(100)
    print('max')

# Wheels

def forward():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    print("forward")

def backward():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    print("backward")

def turn_right():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    print('right')

def turn_left():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

# Camera

def cam_left():
    GPIO.output(in11,GPIO.HIGH)
    GPIO.output(in22,GPIO.LOW)
    print('cam left')
    
def cam_right():
    GPIO.output(in11,GPIO.LOW)
    GPIO.output(in22,GPIO.HIGH)
    print('cam right')

def cam_up():
    GPIO.output(in33,GPIO.LOW)
    GPIO.output(in44,GPIO.HIGH)
    print('cam up')
    
def cam_down():
    GPIO.output(in33,GPIO.HIGH)
    GPIO.output(in44,GPIO.LOW)
    print('cam down')

# Keyboard control

while True:

    x = input()

    if x=='w':
        forward()

    elif x=='s':
        backward()

    elif x=='a':
        turn_left()

    elif x=='d':
        turn_right()

    elif x=='q':
        stop()

    elif x=='1':
        low()

    elif x=='2':
        medium()

    elif x=='3':
        high()
        
    elif x=='4':
        maximum()

    elif x=='i':
        qq.ChangeDutyCycle(100)
        cam_up()
        sleep(.0075)
##        qq.ChangeDutyCycle(75)
##        sleep(.075)
        qq.ChangeDutyCycle(50)
        sleep(.15)
        stop()

    elif x=='k':
        qq.ChangeDutyCycle(100)
        cam_down()
        sleep(.2)
        qq.ChangeDutyCycle(75)
        sleep(.125)
        qq.ChangeDutyCycle(50)
        sleep(.125)
        stop()

    elif x=='j':
        cam_left()

    elif x=='l':
        cam_right()
    
    elif x=='e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
