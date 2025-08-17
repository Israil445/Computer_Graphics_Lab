import turtle

# --- Setup ---
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Visual Surface Detection")

pen = turtle.Turtle()
pen.speed(1)

# -----------------------
# Draw Triangle (same coords)
# -----------------------
def drawTriangle():
    x = [10, 50, 100]
    y = [100, 20, 100]

    pen.penup()
    pen.goto(x[0], y[0])
    pen.pendown()
    pen.fillcolor("green")
    pen.begin_fill()
    pen.goto(x[1], y[1])
    pen.goto(x[2], y[2])
    pen.goto(x[0], y[0])
    pen.end_fill()

# -----------------------
# Draw Circle
# -----------------------
def drawCircle():
    pen.penup()
    pen.goto(100, 100 - 45)  
    pen.pendown()
    pen.fillcolor("blue")
    pen.begin_fill()
    pen.circle(45)
    pen.end_fill()

# -----------------------
# Draw Rectangle
# -----------------------
def drawRectangle():
    x1, y1 = 100, 100
    x2, y2 = 180, 180

    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.fillcolor("red")
    pen.begin_fill()
    pen.goto(x2, y1)
    pen.goto(x2, y2)
    pen.goto(x1, y2)
    pen.goto(x1, y1)
    pen.end_fill()

# -----------------------
# Sequence of drawing
# -----------------------
sequence = "RCT"
for shape in sequence:
    if shape == "C":
        drawCircle()
    elif shape == "T":
        drawTriangle()
    else:
        drawRectangle()

turtle.done()
