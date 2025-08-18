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

# =============================
# Main Program
# =============================

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = turtle.Screen()
screen.title("2D Triangle Translation with Turtle")
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

# Translation factors
tx, ty = (150, 100)

# Compute translated triangle
translated_triangle = []
for point in original_triangle:
    x, y = point           
    new_x = x + tx        
    new_y = y + ty         
    translated_triangle.append((new_x, new_y))
    
# Draw original and translated triangles
draw_triangle(pen, original_triangle, "black", "Original")   
draw_triangle(pen, translated_triangle, "green", "Translated") 

pen.hideturtle()
turtle.done()
