from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)


  

turn(-1) 

for i in range (0,4):
  turn(1)

  for n in range(0,4):
    move()
  turn(1)
  
  for n in range(0,32):
      move()
  turn(-1)
  
  for n in range(0,4):
      move()
  turn(-1)
  
  for n in range(0,32):
      move()
    
