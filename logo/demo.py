from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue"]

for i in range(0,100):
  move(i)
  turn(75)
  color(colors[i%3])