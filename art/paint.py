from tealight.art import (color,rectangle, line, spot, circle, box, image, text, background)

color("black")

sizes = range (3,9)

def ToolBoxThickness (x,y,thicknesses,w,h):
  for t in thicknesses:
    spot(x + w/2, y + h/2, t)
    rectangle(x,y,w,h)
    y = y + h
    
x = 200
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