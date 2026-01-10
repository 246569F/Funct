import turtle
import figures

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Configure the (default) turtle
turtle.speed(5)

# Side length
side_length = 100
b_length = 150

# Draw a square using the function from the other module
figures.draw_square(side_length)
figures.draw_trangle(side_length)
figures.draw_rectangle(side_length, b_length)

# Hide the turtle and finish
turtle.hideturtle()
window.mainloop()
