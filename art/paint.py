from tealight.art import (color,rectangle, line, spot, circle, box, image, text, background)

color("black")

rectangle(10,250,25,25)
spot(22,260,3)


rectangle(10,275,25,25)
spot(22,290,4)

rectangle(10,300,25,25)
spot(22,315,5)

rectangle(10,325,25,25)
spot(22,340,6)

rectangle(10,350,25,25)
spot(22,365,7)

rectangle(10,375,25,25)
spot(22,390,8)

def handle_mousedown(x,y):
  ColNo = (x - 10)/25
  RowNo = (y - 75)/25
  
  print ColNo, RowNo