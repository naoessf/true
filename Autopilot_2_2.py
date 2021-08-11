## import Functions
# import GPS
from GPS import parsing

# import Destinaion
from Destination import Latitude
from Destination import Longitude

# import Motor_Functions
from Motor_Function import gpiosetup
from Motor_Function import dcmotor
from Motor_Function import svmotor
from Motor_Function import forward
from Motor_Function import cleanup

# import math
import math as m

## Destination List
# Numbering of Destination
n = int(input("Number of Destination : "))
 
# Load Function of Destination
latitude = Latitude(n)
longitude = Longitude(n)
print(latitude)
print(longitude)

##Motor Setup
# GPIO Setup
gpiosetup = gpiosetup()
gpiosetup

#DCMotor Setup
dcmotor = dcmotor()
dcmotor
forward = forward()

#SVMotor Setup
svmotor = svmotor()
svmotor

# Move ship
forward

# Float
d1 = 0.0
d2 = 0.0
d3 = 0.0
d4 = 0.0
c1 = 0.0
c2 = 0.0
c3 = 0.0
c4 = 0.0
sc = 0.0


##Main
j = 0
while True:
    # GPS
    position = parsing()
    if position is None:
        pass
    elif position[0] == "$GNRMC":
        j += 1
        if position[4] == "V":
            print("Parsing Number({})".format(j))
            print("Parsing Failed")
        elif position[4] == "A":
            print("Parsing Number({})".format(j))
            print("latitude : {}\tlongitude : {}\tship direction : {}".format(position[1], position[2], position[3]))
            # Ship Point
            x0 = position[2]
            y0 = position[1]
            # Error Range
            e = 0.04166667
            # Movement
            i = 1
            if i <= n :
                #Destination Point
                x1 = float(longitude[i])
                y1 = float(latitude[i])

                #Target Direction
                d1 = 90 - m.atan((y1 - y0)/(x1 - x0))

                d2 = m.atan((y0 - y1)/(x0 - x1)) - 270
                d2 = abs(d2)

                d3 = m.atan((y0 - y1)/(x0 - x1)) - 270
                d3 = abs(d3)

                d4 = -(m.atan((y1 - y0)/(x1 - x0))) - 270
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
                if x1 >= x0 and y1 > y0 :
                    if ds >= d1 :
                        svmot.ChangeDutyCycle((sc * c1) + 7.5)  
                    else :
                        svmot.ChangeDutyCycle(7.5 - (sc * c1))

                #Second quadrant
                elif x0 > x1 and y1 >= y0 :
                    if ds >= d2 :
                        svmot.ChangeDutyCycle((sc * c2) + 7.5)
                    else :
                        svmot.ChangeDutyCycle(7.5 - (sc * c2))

                #Third quadrant
                elif x0 >= x1 and y0 > y1 :
                    if ds >= d3 : #Left
                        svmot.ChangeDutyCycle((sc * c3) + 7.5)
                    else : # ds < d3(Right)
                        svmot.ChangeDutyCycle(7.5 - (sc * c3))

                #Fourth quadrant
                elif x1 > x0 and y0 >= y1 :
                    if ds >= d4 : #Left
                        svmot.ChangeDutyCycle((sc * c4) + 7.5)
                    else : # ds < d4(Right)
                        svmot.ChangeDutyCycle(7.5 - (sc * c4))

                #Finish
                elif y1 - e < y0 < y1 + e and x1 - e < x0 < x1 + e :
                    i += 1
            else:
                break

cleanup = cleanup()
cleanup