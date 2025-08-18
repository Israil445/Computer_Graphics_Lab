import turtle

# =============================
# Helper Functions
# =============================
def draw_pixel(pen, x, y, color="black"):
    pen.penup()
    pen.goto(x, y)
    pen.dot(4, color) 
    pen.pendown()
    
def bresenham_line(pen, x1, y1, x2, y2, color="black"):
    # Ensure left-to-right drawing
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    dx = x2 - x1
    dy = abs(y2 - y1)
    p = 2 * dy - dx

    y = y1
    for x in range(x1, x2 + 1):
        draw_pixel(pen, x, y, color)
        if p >= 0:
            p += 2 * (dy - dx)
            y += 1 if y1 < y2 else -1
        else:
            p += 2 * dy

def draw_axes(pen, width, height):
    pen.pencolor("gray")
    # X-axis
    pen.penup()
    pen.goto(-width//2, 0)
    pen.pendown()
    pen.goto(width//2, 0)
    pen.write("X", align="center", font=("Arial", 12, "normal"))
    
    # Y-axis
    pen.penup()
    pen.goto(0, -height//2)
    pen.pendown()
    pen.goto(0, height//2)
    pen.write("Y", align="center", font=("Arial", 12, "normal"))
    pen.penup()

# =============================
# Main Program
# =============================

# screen setup 
WIDTH, HEIGHT = 800, 600
screen = turtle.Screen()
screen.title("Bresenham Line Drawing with Turtle")
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("white")
screen.tracer(0)  

# pen setup
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.pencolor("black")

# Draw axes for reference
draw_axes(pen, WIDTH, HEIGHT)

# Draw lines using Bresenham algorithm
lines = [
    ((-200, -100), (200, 100)),
    ((-200,100), (200,-100))

]

for (start, end) in lines:
    x0, y0 = start
    x1, y1 = end
    bresenham_line(pen, x0, y0, x1, y1, color="blue")

pen.hideturtle()
turtle.done()

