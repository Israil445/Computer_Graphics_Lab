import turtle

# Setup screen
screen = turtle.Screen()
screen.title("Turtle Coordinate System with Shapes")
screen.bgcolor("white")

# Create turtle
pen = turtle.Turtle()
pen.speed(3)

# --- Draw Axes ---
def draw_axes():
    pen.pensize(2)
    pen.color("black")
    
    # X-axis
    pen.penup()
    pen.goto(-300, 0)
    pen.pendown()
    pen.goto(300, 0)

    # Y-axis
    pen.penup()
    pen.goto(0, -300)
    pen.pendown()
    pen.goto(0, 300)

# --- Draw Shapes ---
def draw_line_up():
    pen.color("red")
    pen.pensize(3)
    pen.penup()
    pen.goto(50, 100)  
    pen.pendown()
    pen.goto(150, 200)  

def draw_square_left():
    pen.color("blue")
    pen.pensize(3)
    pen.penup()
    pen.goto(-200, 100)   
    pen.pendown()
    for _ in range(4):
        pen.forward(80)
        pen.left(90)

def draw_rectangle_down():
    pen.color("green")
    pen.pensize(2)
    pen.penup()
    pen.goto(-200, -200) 
    pen.pendown()
    for _ in range(2):
        pen.forward(120)  
        pen.left(90)
        pen.forward(60)    
        pen.left(90)

def draw_circle_right():
    pen.color("purple")
    pen.pensize(2)
    pen.penup()
    pen.goto(150, -200)   
    pen.pendown()
    pen.circle(60)

# --- Main Execution ---
draw_axes()
draw_line_up()
draw_square_left()
draw_rectangle_down()
draw_circle_right()

# Keep window open
turtle.done()

'''
forward(x) -> Moves forward in the direction the pen is currently facing.
backward(x) -> Moves backward (opposite of the current facing direction).
left(angle) -> Rotates the pen left (counter-clockwise) by the specified angle. Does not move the pen.
right(angle) -> Rotates the pen right (clockwise) by the specified angle. Does not move the pen.

pen.penup()	-> Lifts the pen so it does not draw while moving.
pen.pendown() -> Puts the pen down so it draws while moving.
pen.goto(x, y) -> Moves the pen directly to coordinates (x, y). Draws only if pen is down.
'''