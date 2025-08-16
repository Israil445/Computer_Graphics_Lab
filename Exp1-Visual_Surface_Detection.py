import turtle

# -------------------------
# Constants and Configuration
# -------------------------
WIDTH, HEIGHT = 400, 300
SEQUENCE = "RCT"

# -------------------------
# Shape Drawing Functions
# -------------------------
def draw_triangle(t):
    t.color("green")
    t.penup()
    t.goto(10, 100)
    t.pendown()
    t.begin_fill()
    t.goto(50, 20)
    t.goto(100, 100)
    t.goto(10, 100)
    t.end_fill()

def draw_circle(t):
    t.color("blue")
    t.penup()
    t.goto(100, 55)   
    t.pendown()
    t.begin_fill()
    t.circle(45)
    t.end_fill()

def draw_rectangle(t):
    t.color("red")
    t.penup()
    t.goto(100, 100)
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(80)
        t.right(90)
        t.forward(80)
        t.right(90)
    t.end_fill()

# -------------------------
# Main Function
# -------------------------
def main():
    # Setup screen
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.title("Draw Shapes with Turtle")

    t = turtle.Turtle()
    t.speed(3)

    # Draw shapes based on the sequence
    for shape in SEQUENCE:
        if shape == 'C':
            draw_circle(t)
        elif shape == 'T':
            draw_triangle(t)
        else:
            draw_rectangle(t)

    t.hideturtle()
    screen.mainloop()

# -------------------------
# Entry Point
# -------------------------
if __name__ == "__main__":
    main()
