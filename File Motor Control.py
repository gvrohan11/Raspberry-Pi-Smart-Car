import RPi.GPIO as GPIO          
from time import sleep

##### Front Wheels #####

# Front Left Wheel
in1 = 23
in2 = 24
ena = 25

# Front Right Wheel
in3 = 5
in4 = 6
enb = 13

##### Back Wheels #####

# Back Left Wheel
in5 = 4
in6 = 17
enc = 27

# Back Right Wheel
in7 = 12
in8 = 16
end = 20

GPIO.setmode(GPIO.BCM)

##### Setup #####

# Front Wheels
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p = GPIO.PWM(ena,1000) # Front Left Wheel
q = GPIO.PWM(enb,1000) # Front Right Wheel

# Back Wheels
GPIO.setup(in5,GPIO.OUT)
GPIO.setup(in6,GPIO.OUT)
GPIO.setup(in7,GPIO.OUT)
GPIO.setup(in8,GPIO.OUT)
GPIO.setup(enc,GPIO.OUT)
GPIO.setup(end,GPIO.OUT)
GPIO.output(in5,GPIO.LOW)
GPIO.output(in6,GPIO.LOW)
GPIO.output(in7,GPIO.LOW)
GPIO.output(in8,GPIO.LOW)
r = GPIO.PWM(enc,1000) # Front Left Wheel
t = GPIO.PWM(end,1000) # Front Right Wheel

##### Start #####

p.start(25)
q.start(25)
r.start(25)
t.start(25)

##### Functions #####

def stop():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(in5,GPIO.LOW)
    GPIO.output(in6,GPIO.LOW)
    GPIO.output(in7,GPIO.LOW)
    GPIO.output(in8,GPIO.LOW)
    print("stop")

def forward():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(in5,GPIO.HIGH)
    GPIO.output(in6,GPIO.LOW)
    GPIO.output(in7,GPIO.HIGH)
    GPIO.output(in8,GPIO.LOW)
    print("forward")

def backward():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    GPIO.output(in5,GPIO.LOW)
    GPIO.output(in6,GPIO.HIGH)
    GPIO.output(in7,GPIO.LOW)
    GPIO.output(in8,GPIO.HIGH)
    print("backward")

def turn_right():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    GPIO.output(in5,GPIO.HIGH)
    GPIO.output(in6,GPIO.LOW)
    GPIO.output(in7,GPIO.HIGH)
    GPIO.output(in8,GPIO.LOW)
    print('right')

def turn_left():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(in5,GPIO.HIGH)
    GPIO.output(in6,GPIO.LOW)
    GPIO.output(in7,GPIO.HIGH)
    GPIO.output(in8,GPIO.LOW)
    print('left')

def low():
    p.ChangeDutyCycle(25)
    q.ChangeDutyCycle(25)
    r.ChangeDutyCycle(25)
    t.ChangeDutyCycle(25)
    print('low')

def medium():
    p.ChangeDutyCycle(50)
    q.ChangeDutyCycle(50)
    r.ChangeDutyCycle(50)
    t.ChangeDutyCycle(50)
    print('medium')

def high():
    p.ChangeDutyCycle(75)
    q.ChangeDutyCycle(75)
    print('high')

def maximum():
    p.ChangeDutyCycle(100)
    q.ChangeDutyCycle(100)
    r.ChangeDutyCycle(100)
    t.ChangeDutyCycle(100)
    print('max')

##### Keyboard Control #####

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

    elif x=='e':
        stop()

    elif x=='1':
        low()

    elif x=='2':
        medium()

    elif x=='3':
        high()
        
    elif x=='4':
        maximum()
    
    elif x=='q':
        GPIO.cleanup()
        print("GPIO Clean up")
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")









    
