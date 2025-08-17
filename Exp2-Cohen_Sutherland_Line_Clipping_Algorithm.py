import turtle

# --- Clipping Window Parameters ---
x_left, x_right = 150, 450
y_bottom, y_top = 120, 320

# --- Region Code Constants ---
Left, Right, Bottom, Top = 1, 2, 4, 8


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
            drawLine(x1, y1, x2, y2, "white", pen)
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


# --- Draw a line helper ---
def drawLine(x1, y1, x2, y2, color, pen):
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.pencolor(color)
    pen.goto(x2, y2)


# -----------------------
# Main Program
# -----------------------
screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(3)

# Draw clipping window in yellow
drawLine(x_left, y_bottom, x_right, y_bottom, "yellow", pen)
drawLine(x_right, y_bottom, x_right, y_top, "yellow", pen)
drawLine(x_right, y_top, x_left, y_top, "yellow", pen)
drawLine(x_left, y_top, x_left, y_bottom, "yellow", pen)

# Original line (yellow)
x1, y1, x2, y2 = 120, 50, 350, 400
drawLine(x1, y1, x2, y2, "yellow", pen)

# Clipped line (white)
cohenSutherland(x1, y1, x2, y2, pen)

turtle.done()
