from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)


def eatvertical():
  for n in range(0,32):
    move()
turn(1)    

def eathorizontal():
  for n in range(0,32):
    move()
    
turn(1)


eatvertical()
eathorizontal()