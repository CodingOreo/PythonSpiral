import turtle

# Variables
x_start_cord = -200 # X Starting coordinate
y_start_cord = 0 # Y Starting coordinate 
num_lines = 60 # number of lines to draw
line_length = 400 #length of each line 
angle = 170 # Angle to turn 
animation_speed = 0 # Animation Speed

# Move turtle to it's initial position
turtle.hideturtle()
turtle.penup()
turtle.goto(x_start_cord, y_start_cord)
turtle.pendown()

# set animation speed
turtle.speed(animation_speed)

# Draw 36 lines with the turtle tilted by 170 degrees after each drawn line 
for x in range(num_lines):
    turtle.forward(line_length)
    turtle.left(angle)
