import turtle
import figures

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Configure the (default) turtle
pen = turtle.Turtle()
pen.speed(5)

# Side length
side_length = 100
b_length = 150

# Draw a square using the function from the other module
def draw_square(length):
    for _ in range(4):
        pen.forward(length)
        pen.right(90)
def draw_trangle(length):
    for _ in range(3):
        pen.forward(length)
        pen.right(120)
def draw_rectangle(lenght_a, lenght_b):
    for _ in range(2):
        pen.forward(lenght_a)
        pen.right(90)
        pen.forward(lenght_b)
        pen.right(90)

draw_square(side_length)
pen.penup()
pen.goto(-100,0)
pen.pendown()
draw_trangle(side_length)
pen.penup()
pen.goto(-200,0)
pen.pendown()
draw_rectangle(side_length, b_length)
pen.penup()
pen.goto(0,-300)
pen.pendown()
draw_square(side_length)
pen.penup()
pen.goto(-100,-300)
pen.pendown()
draw_trangle(side_length)
pen.penup()
pen.goto(-200,-300)
pen.pendown()
draw_rectangle(side_length, b_length)
# Hide the turtle and finish
pen.hideturtle()
window.mainloop()
