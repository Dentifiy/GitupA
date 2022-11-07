import math

#read UP, DOWN, LEFT, and RIGHT
UP = int(input("Enter UP: "))
DOWN = int(input("Enter DOWN: "))
LEFT = int(input("Enter LEFT: "))
RIGHT = int(input("Enter RIGHT: "))

x = 0
y = 0
d = 0

#calculate the distance
if UP>DOWN:
    y = UP-DOWN
    if LEFT>RIGHT:
        x = LEFT-RIGHT
        d = int(round((math.sqrt(x*x+y*y)), 0))
        print("It is in Left and Up direction")
        print("The distance is", d)
    else:
        x = RIGHT-LEFT
        d = int(round((math.sqrt(x*x+y*y)), 0))
        print("It is in Right and Up direction")
        print("The distance is", d)
else:
    y = DOWN-UP
    if LEFT>RIGHT:
        x = LEFT-RIGHT
        d = int(round((math.sqrt(x*x+y*y)), 0))
        print("It is in Left and Down direction")
        print("The distance is", d)
    else:
        x = RIGHT-LEFT
        d = int(round((math.sqrt(x*x+y*y)), 0))
        print("It is in Right and Down direction")
        print("The distance is", d)
