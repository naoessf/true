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
            e = 0.016666668
            # Movement
            i = 1
            if i <= n :
                #Destination Point
                x1 = float(longitude[i])
                y1 = float(latitude[i])

                ds = position[3] 

                dx = abs(atan((y0 - y1) / (x0 - x1)))

                sc = (1.5 / 180)
                
                a = abs(dx - ds)

                if dx >= ds :
                    svmot.ChangeDutyCycle((sc * a) + 7.5)
                elif dx < ds:
                    svmot.ChangeDutyCycle(7.5 - (sc * a))

                #finish
                elif y1 - e < y0 < y1 + e and x1 - e < x0 < x1 + e :
                    i += 1
            else:
                break

cleanup = cleanup()
cleanup