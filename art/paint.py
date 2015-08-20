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

sizes = [3,4,5,6,7,8]

def ToolBoxThickness (x,y,thicknesses,w,h):
  for t in thicknesses:
    spot(x,y,t)
    rectangle(x,y,w,h)
    y = y + h
    
x = 300
y =310
w = 25
h = 25
ToolBoxThickness(x,y,sizes,w,h)
    
  











  

def handle_mousedown(x,y):
  ColNo = (x - 10)/25
  RowNo = (y - 300)/25
  
  print ColNo, RowNo
  
  if ColNo == 0 and RowNo == 0:
    print 3
  elif ColNo == 0 and RowNo == 1:
    print 4
  if ColNo == 0 and RowNo == 2:
    print 5
  elif ColNo == 0 and RowNo == 3:
    print 6 
  if ColNo == 0 and RowNo == 4:
    print 7
  elif ColNo == 0 and RowNo == 5:
    print 8 