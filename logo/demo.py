from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue"]

for i in range(50,100):
  move(i)
  turn(91)
  color(colors[i%3])