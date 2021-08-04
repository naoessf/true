import math as m 
import operator
import RPi.GPIO as GPIO
from time import sleep
import GPS 
import Destination
import Destination_Test

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

#Ship Point
x0 = position[2]
y0 = position[1]


#Error Range
e = 0.04166667

i = 0

while i < len(lat_list) :
    #Destination Point
    x1 = lon_list[i]
    y1 = lat_list[i]

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

        #svmot.change
        c1 = abs(ds - d1)
        c2 = abs(ds - d2)
        c3 = abs(ds - d3)
        c4 = abs(ds - d4)

        sc = (1.5 / 180)

            #First quadrant
            if x0 >= x1 and y0 > y1 :
                if ds >= d1 : #Left
                    svmot.ChangeDutyCycle((sc * c1) + 7.5)
                else : # ds < d1(Right)
                    svmot.ChangeDutyCycle(7.5 - (sc * c1))

            #Second quadrant
            elif x0 < x1 and y0 >= y1 :
                if ds >= d2: #Left
                    svmot.ChangeDutyCycle((sc * c2) + 7.5)
                else : # ds < d2(Right)
                    svmot.ChangeDutyCycle(7.5 - (sc * c2))

            #Third quadrant
            elif x1 >= x0 and y0 < y1 :
                if ds >= d3 : #Left
                    svmot.ChangeDutyCycle((sc * c3) + 7.5)
                else : # ds < d3(Right)
                    svmot.ChangeDutyCycle(7.5 - (sc * c3))

            #Fourth quadrant
            elif x0 > x1 and y1 >= y0 :
                if ds >= d4 : #Left
                    svmot.ChangeDutyCycle((sc * c4) + 7.5)
                else : # ds < d4(Right)
                    svmot.ChangeDutyCycle(7.5 - (sc * c4))

            #Finish
            elif y1 - e < y0 < y1 + e and x1 - e < x0 < x1 + e :
                svmot.stop()
                dcmot.stop()
                GPIO.cleanup()
                i += 1
    
