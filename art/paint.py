from tealight.art import (color,rectangle, line, line_width, spot, circle, box, image, text, background)

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
    
def handle_mousedown(mx,my):
  if mx > x and mx < x+w and my > y +(h*len(sizes)):
    RowNo = (my - y)/h
   
    line_width(sizes[RowNo])
    print RowNo
    


  
   
  
  
  
