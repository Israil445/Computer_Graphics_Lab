import turtle

# =============================
# Helper Functions
# =============================
def draw_pixel(pen, x, y, color="black"):
    pen.penup()
    pen.goto(x, y)
    pen.dot(4, color)
    pen.pendown()

def midpoint_circle(pen, xc, yc, r, color="black"):
    x = 0
    y = r
    p = 1 - r  
    def plot_circle_points(xc, yc, x, y):
        # Draw all 8 symmetric points
        draw_pixel(pen, xc + x, yc + y, color)
        draw_pixel(pen, xc - x, yc + y, color)
        draw_pixel(pen, xc + x, yc - y, color)
        draw_pixel(pen, xc - x, yc - y, color)
        draw_pixel(pen, xc + y, yc + x, color)
        draw_pixel(pen, xc - y, yc + x, color)
        draw_pixel(pen, xc + y, yc - x, color)
        draw_pixel(pen, xc - y, yc - x, color)
        
    plot_circle_points(xc, yc, x, y)
    
    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        plot_circle_points(xc, yc, x, y)

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

# Setup screen
WIDTH, HEIGHT = 800, 600
screen = turtle.Screen()
screen.title("Midpoint Circle Drawing with Turtle")
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("white")
screen.tracer(0)

# Setup pen
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.pencolor("black")

draw_axes(pen, WIDTH, HEIGHT)

# Example circles: (center_x, center_y, radius)
circles = [(0, 0, 100), (-150, 50, 50), (200, -100, 75)]

for xc, yc, r in circles:
    midpoint_circle(pen, xc, yc, r, color="blue")

pen.hideturtle()
turtle.done()
