from tealight.art import (color,rectangle, line, line_width, spot, circle, box, image, text, background)

color("black")

sizes = range (3,36,3)

def ToolBoxThickness (x,y,thicknesses,w,h):
  for t in thicknesses:
    spot(x + w/2, y + h/2, t)
    rectangle(x,y,w,h)
    y = y + h
    
x = 85
y =5
w = 70
h = 70
ToolBoxThickness(x,y,sizes,w,h)
    
def thick_click(mx,my):
  if mx > x and mx < x+w and my > y and my < y +(h*len(sizes)):
    RowNo = (my - y)/h
   
    line_width(sizes[RowNo])
    print RowNo
    


  
   
  
  
  
