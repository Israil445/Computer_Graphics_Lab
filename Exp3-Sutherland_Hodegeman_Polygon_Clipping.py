import turtle

# --- Point structure equivalent ---
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# --- Clipping window ---
wMin = Point(100, 100)
wMax = Point(300, 250)

# -------------------------
# Check if point is inside a clip edge
# edge: 0=LEFT, 1=RIGHT, 2=BOTTOM, 3=TOP
# -------------------------
def inside(p, edge):
    if edge == 0: return p.x >= wMin.x      # LEFT
    elif edge == 1: return p.x <= wMax.x    # RIGHT
    elif edge == 2: return p.y >= wMin.y    # BOTTOM
    else: return p.y <= wMax.y              # TOP

# -------------------------
# Intersection with clip edge
# -------------------------
def intersect(p1, p2, edge):
    m = (p2.y - p1.y) / (p2.x - p1.x) if p1.x != p2.x else 1e9
    if edge == 0:  # LEFT
        x = wMin.x
        y = p1.y + (wMin.x - p1.x) * m
    elif edge == 1:  # RIGHT
        x = wMax.x
        y = p1.y + (wMax.x - p1.x) * m
    elif edge == 2:  # BOTTOM
        y = wMin.y
        x = p1.x + (wMin.y - p1.y) / m if m != 0 else p1.x
    else:  # TOP
        y = wMax.y
        x = p1.x + (wMax.y - p1.y) / m if m != 0 else p1.x
    return Point(x, y)

# -------------------------
# Clip polygon against one edge
# -------------------------
def clip(poly, edge):
    res = []
    n = len(poly)
    for i in range(n):
        curr = poly[i]
        prev = poly[(i - 1 + n) % n]
        ci, pi = inside(curr, edge), inside(prev, edge)

        if ci and pi:
            res.append(curr)
        elif not pi and ci:
            res.append(intersect(prev, curr, edge))
            res.append(curr)
        elif pi and not ci:
            res.append(intersect(prev, curr, edge))
    return res

# -------------------------
# Drawing helpers
# -------------------------
def drawPoly(poly, color):
    if not poly:
        return
    pen.pencolor(color)
    pen.penup()
    pen.goto(poly[0].x, poly[0].y)
    pen.pendown()
    for p in poly[1:]:
        pen.goto(p.x, p.y)
    pen.goto(poly[0].x, poly[0].y)

def drawWindow():
    pen.pencolor("white")
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
screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(3)
pen.hideturtle()

# Define star polygon
star = [
    Point(200, 300), Point(250, 220), Point(330, 220), Point(260, 170),
    Point(300, 80), Point(200, 130), Point(100, 80), Point(140, 170),
    Point(70, 220), Point(150, 220)
]

# Draw clipping window and original polygon
drawWindow()
drawPoly(star, "white")

# Sequentially clip against edges
edges = [0, 1, 2, 3]  # LEFT, RIGHT, BOTTOM, TOP
colors = ["red", "yellow", "cyan", "green"]

for i, edge in enumerate(edges):
    screen.update()
    star = clip(star, edge)
    drawPoly(star, colors[i])

turtle.done()
