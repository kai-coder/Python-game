def drawCircle(size):
    import turtle
    turtle.speed(0)
    turtle.circle(size)
    turtle.done()
def drawRectangle(width, height):
    import turtle
    turtle.speed(0)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.done()