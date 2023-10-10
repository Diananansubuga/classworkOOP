# write a procedual programme then convert it to an object oriented programme
import tkinter as tk

class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center = [center_x, center_y]
        self.radius = radius

    def __repr__(self):
        return f"Circle(center={self.center}, radius={self.radius})"

    def draw(self, canvas):
        rad = self.radius
        x1 = self.center[0] - rad
        x2 = self.center[1] - rad
        y1 = self.center[0] + rad
        y2 = self.center[1] + rad

        canvas.create_oval(x1, x2, y1, y2, fill='green')

    def move(self, x, y):
        self.center = [x, y]

# Create a Tkinter window
tab = tk.Tk()
tab.title("Circle Drawing")

# Create a canvas to draw on
canvas = tk.Canvas(tab, width=400, height=800)
canvas.pack()

# Create a Circle object and draw it on the canvas
circle = Circle(200, 200, 40)
circle.draw(canvas)

# Run the Tkinter main loop
tab.mainloop()
