import turtle
import time
import math

# =============================
# snowflake pattern Draw Function
# =============================
def draw_snowflake_pattern(pen, start, end, depth):
    if depth == 0:
        pen.penup()
        pen.goto(start)
        pen.pendown()
        pen.goto(end)
        time.sleep(0.01)  
        screen.update()
        return

    # Divide the segment into three equal parts
    dx = (end[0] - start[0]) / 3
    dy = (end[1] - start[1]) / 3

    # First point at one-third
    p1 = (start[0] + dx, start[1] + dy)
    
    # Third point at two-thirds
    p3 = (start[0] + 2 * dx, start[1] + 2 * dy)

    # Calculate the peak of the equilateral triangle
    px = p1[0] + (p3[0] - p1[0]) / 2 + math.sqrt(3) * (p3[1] - p1[1]) / 2
    py = p1[1] + (p3[1] - p1[1]) / 2 - math.sqrt(3) * (p3[0] - p1[0]) / 2
    p2 = (px, py)

    # Recursively draw the four segments
    draw_snowflake_pattern(pen, start, p1, depth - 1)
    draw_snowflake_pattern(pen, p1, p2, depth - 1)
    draw_snowflake_pattern(pen, p2, p3, depth - 1)
    draw_snowflake_pattern(pen, p3, end, depth - 1)
    
# =============================
# Main program
# =============================

#setup the screen
WIDTH, HEIGHT = 800, 600
screen = turtle.Screen()
screen.title("Snowflake Pattern with Turtle")
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("white")
screen.tracer(0)

# setup the pen
pen = turtle.Turtle()
pen.hideturtle()
pen.pensize(3)
pen.pencolor("green")
pen.speed(0)

# Define Triangle Points
p0 = (0, 250)
p1 = (-200, -100)
p2 = (200, -100)

# Draw Koch Snowflake
recursion_depth = 3
draw_snowflake_pattern(pen, p0, p1, recursion_depth)
draw_snowflake_pattern(pen, p1, p2, recursion_depth)
draw_snowflake_pattern(pen, p2, p0, recursion_depth)

# Final update and keep window open
screen.update()
screen.mainloop()
