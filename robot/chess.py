from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

def robot (side):
    for i in range(0,3):
    move(side)
    turn(120)