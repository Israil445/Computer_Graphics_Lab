import turtle

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

def scale_triangle(triangle, sx, sy, pivot):
    xp, yp = pivot
    scaled = []
    for x, y in triangle:
        # Translate point relative to pivot
        x_shift = x - xp
        y_shift = y - yp
        # Apply scaling
        new_x = xp + x_shift * sx
        new_y = yp + y_shift * sy
        scaled.append((new_x, new_y))
    return scaled

# =============================
# Main Program
# =============================

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = turtle.Screen()
screen.title("2D Triangle Scaling with Turtle")
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

# Scaling settings
sx, sy = 1.5, 0.8        
pivot_point = (100, 50) 

# Compute scaled triangle
scaled_triangle = scale_triangle(original_triangle, sx, sy, pivot_point)

# Draw original and scaled triangles
draw_triangle(pen, original_triangle, "black")   
draw_triangle(pen, scaled_triangle, "green") 

pen.hideturtle()
turtle.done()
