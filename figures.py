import turtle

# Draw a square
def draw_square(length):
    for _ in range(4):
        turtle.forward(length)
        turtle.right(90)
def draw_trangle(length):
    for _ in range(3):
        turtle.forward(length)
        turtle.right(120)
def draw_rectangle(lenght_a, lenght_b):
    for _ in range(2):
        turtle.forward(lenght_a)
        turtle.right(90)
        turtle.forward(lenght_b)
        turtle.right(90)