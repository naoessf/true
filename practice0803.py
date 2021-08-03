import math as m 
import operator
import RPi.GPIO as GPIO
from time import sleep
import GPS 

#GPIO setup
#GPIO11 : Servo
#GPIO12 : DC
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
LED = 36
GPIO.setup(36, GPIO.OUT, initial=GPIO.LOW)
svmot = GPIO.PWM(11, 50)
dcmot = GPIO.PWM(12, 50)
svmot.start(0)
dcmot.start(0)
svmot.ChangeDutyCycle(7.5)
dcmot.ChangeDutyCycle(7.5)

#Target Point
x10 = str(input("first point longitude(raw_data) :")
x11 = (x10[0:2])
x11 = float(x11)
x12 = (x10[2:])
x12 = float(x12)
x1 = x11 + x12

y10 = str(input("first point latitude(law_data) :"))
y11 = (y10[0:2])
y11 = float(y11)
y12 = (y10[2:])
y12 = float(y12)
y1 = y11 + y12

#Ship Point
x0 = position[2]
y0 = position[1]

#Target Direction
d1 = m.atan((y0 - y1)/(x0 - x1)) - 270
d1 = abs(d1)

d2 = m.atan((y1 - y0)/(x1 - x0)) - 270
d2 = abs(d2)

d3 = 90 - m.atan((y1 - y0)/(x1 - x0))

d4 = m.atan((y0 - y1)/(x0 - x1)) - 180 
d4 = abs(d4)

#Ship Direction
ds = position[3]

#First quadrant
if x0 >= x1 and y0 > y1 :
    if ds > d1 :
        Left
    else : # ds < d1
        Right

#Second quadrant
elif x0 < x1 and y0 >= y1 :
    if ds > d2:
        Left
    else : # ds < d2
        Right

#Third quadrant
elif x1 >= x0 and y0 < y1 :
    if ds > d3 :
        Left
    else : # ds < d3
        Right

#Fourth quadrant
elif x0 > x1 and y1 >= y0 :
    if ds > d4 :
        Left
    else : # ds < d4
        Right

#Finish
elif x0 = x1 and y0 = y1 :
    svmot.stop()
    dcmot.stop()
    GPIO.cleanup()
