'''
Day 6 topics:
-functions
-while loops
-Karel the robot
'''

#hurdle race

def turnRight():
    turnLeft()
    turnLeft()
    turnLeft()

def jump():
    move()
    turnLeft()
    move()
    turnRight()
    move()
    turnRight()
    move()
    turnLeft()


while not atGoal():
    jump()
