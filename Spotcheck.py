#Paul Njenje
#24/09/2014
#Spot Check q1

print("Finding the dimentions of a pool with a semicircle on one side. In metres:")

width = int(input("What is the Width: "))
lenght = int(input("What is the Lenght: "))
depth = int(input("What is the Depth: "))

mainSectionVolume = lenght * width * depth
circleRadius = width / 2
circleArea = 3.14 * (circleRadius * circleRadius)
halfCircleVolume = (circleArea / 2) * depth

poolVolume = mainSectionVolume + halfCircleVolume

print ("Volume ot this pool is {0}m cubed".format(poolVolume))

