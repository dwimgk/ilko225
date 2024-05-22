from turtle import Turtle, Screen
from PIL import Image

def dragging(x,y):
    yertle.ondrag(None)
    yertle.setheading(yertle.towards(x,y))
    yertle.goto(x,y)
    yertle.ondrag(dragging)

def save_dr():
    screen.onkey(None, "s")
    filename = "00drawing.eps"
    screen.getcanvas().postscript(file=filename)
    img = Image.open("00drawing.eps")
    img.save("00turtle.png", "png")
    print("Saved")

screen = Screen()

yertle = Turtle('turtle')
yertle.speed('fastest')
yertle.width(50)
yertle.penup()
yertle.goto(150, 250)
yertle.pendown()

yertle.ondrag(dragging)

screen.onkey(save_dr, "s")
screen.listen()

screen.mainloop()