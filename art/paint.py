from tealight.art import (color,rectangle, line, spot, circle, box, image, text, background)

color("black")

rectangle(10,300,25,25)
spot(22,310,3)

rectangle(10,325,25,25)
spot(22,340,4)

rectangle(10,350,25,25)
spot(22,365,5)

rectangle(10,375,25,25)
spot(22,390,6)

rectangle(10,400,25,25)
spot(22,415,7)

rectangle(10,425,25,25)
spot(22,440,8)

def handle_mousedown(x,y):
  ColNo = (x - 10)/25
  RowNo = (y - 300)/25
  
  print ColNo, RowNo
  
  if ColNo == 0 and RowNo == 0:
    print 