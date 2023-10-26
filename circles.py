

import tkinter as tk
class Circle(object):
    def __init__(self,center,radius):
        self.center=center,
        self.radius=radius

    def draw(self,canvas):
        rad=self.radius
        x1=self.center[0]-rad
        x2=self.center[1]-rad
        y1=self.center[0]+rad
        y2=self.center[1]+rad

        canvas.create_oval(x1,x2,y1,y2, fill='red')
    
    def move(self,x,y):
        self.center=[x,y]
    
window = tk.Tk()
window.title("Circle Drawing")

# Create a canvas to draw on
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Create a Circle object and draw it on the canvas
circle = Circle( 200, 50)
circle.draw(canvas)

# Run the Tkinter main loop
window.mainloop()           





