import turtle
import math

# =============================
# Helper Functions
# =============================
def draw_triangle(pen, triangle, color, label=None):
    pen.pencolor(color)
    pen.penup()
    pen.goto(triangle[0][0], triangle[0][1])
    
    pen.pendown()
    # Draw the triangle edges
    pen.goto(triangle[1][0], triangle[1][1])
    pen.goto(triangle[2][0], triangle[2][1])
    pen.goto(triangle[0][0], triangle[0][1])  
    pen.penup()
    
    # Draw label if provided
    if label:
        pen.goto(triangle[0][0] - 20, triangle[0][1] + 20)
        pen.write(label)

def draw_axes(pen, width, height):
    # X-axis
    pen.penup()
    pen.goto(-width / 2, 0)
    pen.pendown()
    pen.goto(width / 2, 0)
    pen.write("X")

    # Y-axis
    pen.penup()
    pen.goto(0, -height / 2)
    pen.pendown()
    pen.goto(0, height / 2)
    pen.write("Y")
    
    pen.penup()

def rotate_triangle(triangle, angle_deg, pivot):
    xp, yp = pivot
    angle_rad = math.radians(angle_deg)
    cos_theta = math.cos(angle_rad)
    sin_theta = math.sin(angle_rad)
    
    rotated = []
    for x, y in triangle:
        # Translate(shift) point relative to pivot
        x_shift = x - xp
        y_shift = y - yp
        # Apply rotation
        new_x = xp + (x_shift * cos_theta - y_shift * sin_theta)
        new_y = yp + (x_shift * sin_theta + y_shift * cos_theta)
        rotated.append((new_x, new_y))
    
    return rotated

# =============================
# Main Program
# =============================

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = turtle.Screen()
screen.title("2D Triangle Rotation with Turtle")
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.pencolor("black")

# Draw axes
draw_axes(pen, WIDTH, HEIGHT)

# Define triangle vertices
original_triangle = [(50, 50), (150, 50), (100, 120)]

# Rotation settings
angle = 45       
pivot_point = (100, 50)  

# Compute rotated triangle
rotated_triangle = rotate_triangle(original_triangle, angle, pivot_point)

# Draw original and rotated triangles
draw_triangle(pen, original_triangle, "black", "Original")   
draw_triangle(pen, rotated_triangle, "red", "Rotated") 

pen.hideturtle()
turtle.done()
