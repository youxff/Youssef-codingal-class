import turtle

paper = turtle.Screen()
paper.bgcolor("black")
paper.title("Neon Mandala")

# PART 2 - CREATE THE TURTLE PEN
pen = turtle.Turtle()
pen.speed("fastest")
pen.hideturtle() # hides the arrow shape

# PART 3 - OUTER COLOR SPIRAL (MOVEMENT + LOOPS + COLOR)
colors = ["red", "orange", "yellow", "lime", "cyan", "violet", "pink", "white"]

for i in range(80):
    pen.color(colors[i % len(colors)]) # cycles through the color list endlessly.
    pen.width(2)
    pen.forward(i * 2)
    pen.right(91)

# PART 4 - PEN CONTROL: MOVE TO THE CENTER AND DRAW A FILLED STAR
pen.penup()
pen.goto(0, -60)
pen.setheading(90)
pen.pendown()
pen.color("gold", "yellow")
pen.begin_fill()

for i in range(5):
    pen.forward(130)
    pen.right(144)

pen.end_fill()

# PART 5 - INNER PETAL RING (NESTED LOOP + FILL)
# the outer loop spins around 360 degrees (36 petals x 10 degrees each).
# the inner loop drawa one square petal each rotation.
# Nesting loops inside loops is how complex patterns are built!
pen.penup()
pen.goto(0, 0)
pen.pendown()
petal_colors = ["cyan", "lime", "violet", "orange", "deeppink"]

for i in range(36):
    pen.color(petal_colors[i % len(petal_colors)],
              petal_colors[(i + 2) % len(petal_colors)])

    pen.begin_fill()

    for j in range(4):
        pen.forward(55)
        pen.right(90)

    pen.end_fill()
    pen.right(10)

# KEEP WINDOW OPEN
turtle.done()