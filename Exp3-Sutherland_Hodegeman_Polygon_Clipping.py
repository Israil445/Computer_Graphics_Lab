import turtle

# Point structure equivalent 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Clipping window 
wMin = Point(100, 100)
wMax = Point(300, 250)

# Clipping edge constants
LEFT, RIGHT, BOTTOM, TOP = 0, 1, 2, 3

# Check if point is inside a clip edge
def inside(p, edge):
    if edge == LEFT:
        return p.x >= wMin.x
    elif edge == RIGHT:
        return p.x <= wMax.x
    elif edge == BOTTOM:
        return p.y >= wMin.y
    elif edge == TOP:
        return p.y <= wMax.y         


# Intersection with clip edge
def intersect(p1, p2, edge):
    m = (p2.y - p1.y) / (p2.x - p1.x) if p1.x != p2.x else 1e9
    if edge == 0: 
        x = wMin.x
        y = p1.y + (wMin.x - p1.x) * m
    elif edge == 1:  
        x = wMax.x
        y = p1.y + (wMax.x - p1.x) * m
    elif edge == 2:  
        y = wMin.y
        x = p1.x + (wMin.y - p1.y) / m if m != 0 else p1.x
    else:  
        y = wMax.y
        x = p1.x + (wMax.y - p1.y) / m if m != 0 else p1.x
    return Point(x, y)

# Clip polygon against one edge
def clip_polygon(points, edge):
    clipped = []
    for i in range(len(points)):
        curr = points[i]
        prev = points[i - 1]
        curr_in = inside(curr, edge)
        prev_in = inside(prev, edge)

        if prev_in and curr_in:
            clipped.append(curr)
        elif not prev_in and curr_in:
            clipped.append(intersect(prev, curr, edge))
            clipped.append(curr)
        elif prev_in and not curr_in:
            clipped.append(intersect(prev, curr, edge))
    return clipped

# Drawing helpers
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
    
def draw_polygon(poly, color):
    if not poly:
        return
    pen.pencolor(color)
    pen.penup()
    pen.goto(poly[0].x, poly[0].y)
    pen.pendown()
    for p in poly[1:]:
        pen.goto(p.x, p.y)
    pen.goto(poly[0].x, poly[0].y)

def draw_clip_window(pen):
    pen.pencolor("green")
    pen.penup()
    pen.goto(wMin.x, wMin.y)
    pen.pendown()
    pen.goto(wMax.x, wMin.y)
    pen.goto(wMax.x, wMax.y)
    pen.goto(wMin.x, wMax.y)
    pen.goto(wMin.x, wMin.y)

# -------------------------
# Main program
# -------------------------

# Setup turtle screen
WIDTH, HEIGHT = 800, 600
screen = turtle.Screen()
screen.title("Cohen-Sutherland Line Clipping")
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("white")

# pen setup
pen = turtle.Turtle()
pen.speed(3)
pen.pensize(2)
pen.pencolor("Black")

# Define star polygon
star = [
    Point(200, 300), Point(250, 220), Point(330, 220), Point(260, 170),
    Point(300, 80), Point(200, 130), Point(100, 80), Point(140, 170),
    Point(70, 220), Point(150, 220)
]

# Draw scene
draw_axes(pen, WIDTH, HEIGHT)
draw_clip_window(pen)
draw_polygon(star, "black")

# Step-by-step clipping
edges = [LEFT, RIGHT, BOTTOM, TOP]
colors = ["red", "blue", "cyan", "green"]

for i, edge in enumerate(edges):
    screen.update()
    star = clip_polygon(star, edge)
    draw_polygon(star, colors[i])
    
pen.hideturtle()
turtle.done()
