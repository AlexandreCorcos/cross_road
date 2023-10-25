
import turtle

# Define a list of 11 different colors
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "gray", "black", "white"]

# Create a turtle object
t = turtle.Turtle()

# Set the turtle's speed
t.speed(0)

# Loop through the list of colors
for color in colors:
    # Set the turtle's color to the current color
    t.color(color)

    # Move the turtle forward
    t.forward(100)

    # Turn the turtle right
    t.right(30)

# Hide the turtle
t.hideturtle()

# Exit the turtle graphics window
turtle.done()
