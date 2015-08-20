from tealight.art import (color, line, spot, circle, box, image, text, background)

def DrawPalette(x,y, colors, w, h):
  for c in colors:
    color(c)
    box(x, y, w, h)
    y = y + h
 
 colors = ["black", "grey"]
 
x = 100
y = 75
w = 25
DrawPalette(x,y, colors, w, h)

def handle_mousedown(mx,my):
  if mx>x and mx < x+w and my>y and my < y+(h*len(colors)):
    
    RowNo = (my-y)/h
    
    print RowNo
    print colors[RowNo]
   
   return