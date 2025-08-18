import turtle
import math

# ===================== Math Utilities =====================
def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)

def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

# Bernstein ploynomial
def bezier_basis(k, n, u):
    return nCr(n, k) * (u ** k) * ((1 - u) ** (n - k))

# ===================== Bezier Curve Function =====================
def bezier_curve(pen, points, steps=1000):
    n = len(points) - 1
    pen.pencolor("green")
 
    # Draw curve
    pen.penup()
    for i in range(steps + 1):
        u = i / steps
        x, y = 0, 0
        for k in range(n + 1):
            b = bezier_basis(k, n, u)
            x += points[k][0] * b
            y += points[k][1] * b
        if i == 0:
            pen.goto(x, y)
            pen.pendown()
        else:
            pen.goto(x, y)

    # Draw control points
    pen.pencolor("red")
    pen.penup()
    for (x, y) in points:
        pen.goto(x, y-3)  
        pen.pendown()
        pen.circle(3)      
        pen.penup()

    # Draw control polygon
    pen.pencolor("gray")
    pen.penup()
    pen.goto(points[0])
    pen.pendown()
    for (x, y) in points[1:]:
        pen.goto(x, y)

# Draw axes
def draw_axes(pen, width, height):
    pen.penup()
    pen.goto(-width / 2, 0)
    pen.pendown()
    pen.goto(width / 2, 0)
    pen.write("X")

    pen.penup()
    pen.goto(0, -height / 2)
    pen.pendown()
    pen.goto(0, height / 2)
    pen.write("Y")
    pen.penup()

# ===================== Main =====================
# screen stup
WIDTH, HEIGHT = 800, 600
screen = turtle.Screen()
screen.title("Bezier Curve using Python Turtle")
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("white")
screen.tracer(0)  

# pen setup
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.pencolor("Black")
draw_axes(pen, WIDTH, HEIGHT)

# control points
control_points = [(27, 243), (101, 47), (324, 197), (437, 23)]

# Draw bezier curve
bezier_curve(pen, control_points, steps=1000)

pen.hideturtle()
screen.update()
turtle.done()