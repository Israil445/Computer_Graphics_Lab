import turtle

# Clipping Window Parameters 
x_left, x_right = -100, 300
y_bottom, y_top = -50, 200

# Region Codes 
Left, Right, Bottom, Top = 1, 2, 4, 8

# Draw axes
def draw_axes(pen, width, height):
    pen.penup()
    pen.goto(-width / 2, 0)
    pen.pendown()
    pen.goto(width / 2, 0)
    pen.write("X", align="center", font=("Arial", 12, "normal"))

    pen.penup()
    pen.goto(0, -height / 2)
    pen.pendown()
    pen.goto(0, height / 2)
    pen.write("Y", align="center", font=("Arial", 12, "normal"))
    pen.penup()

# Function to calculate region code for a point
def regionCode(x, y):
    code = 0
    if x > x_right:
        code |= Right
    elif x < x_left:
        code |= Left
    if y > y_top:
        code |= Top
    elif y < y_bottom:
        code |= Bottom
    return code


# Cohen-Sutherland Line Clipping Algorithm
def cohenSutherland(x1, y1, x2, y2, pen):
    code1 = regionCode(x1, y1)
    code2 = regionCode(x2, y2)

    while True:
        if not (code1 | code2):  # Line completely inside
            drawLine(x1, y1, x2, y2, "green", pen)
            return
        elif code1 & code2:  # Line completely outside
            return
        else:  # Line partially inside
            code = code1 if code1 else code2

            if code & Top:
                y = y_top
                x = x1 + (x2 - x1) * (y - y1) / (y2 - y1)
            elif code & Bottom:
                y = y_bottom
                x = x1 + (x2 - x1) * (y - y1) / (y2 - y1)
            elif code & Left:
                x = x_left
                y = y1 + (y2 - y1) * (x - x1) / (x2 - x1)
            elif code & Right:
                x = x_right
                y = y1 + (y2 - y1) * (x - x1) / (x2 - x1)

            if code == code1:
                x1, y1 = x, y
                code1 = regionCode(x1, y1)
            else:
                x2, y2 = x, y
                code2 = regionCode(x2, y2)


# Draw a line helper 
def drawLine(x1, y1, x2, y2, color, pen):
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.pencolor(color)
    pen.goto(x2, y2)

#------------------------------
# Main Function
#------------------------------
# screen stup
WIDTH, HEIGHT = 800, 600
screen = turtle.Screen()
screen.title("Cohen-Sutherland Line Clipping")
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("white")

# pen setup
pen = turtle.Turtle()
pen.speed(2)
pen.pensize(2)
pen.pencolor("Black")
draw_axes(pen, WIDTH, HEIGHT)


# Draw the clipping rectangle
drawLine(x_left, y_bottom, x_right, y_bottom, "green", pen)
drawLine(x_right, y_bottom, x_right, y_top, "green", pen)
drawLine(x_right, y_top, x_left, y_top, "green", pen)
drawLine(x_left, y_top, x_left, y_bottom, "green", pen)

# Original line
x1, y1, x2, y2 = -180, -30, 300, 300
drawLine(x1, y1, x2, y2, "red", pen)

# Clipped line 
cohenSutherland(x1, y1, x2, y2, pen)

pen.hideturtle()
turtle.done()
