import turtle
wn = turtle.Screen()
tess = turtle.Turtle()
class WatchedKey:
    def __init__(self, key):
        self.key = key
        self.down = False
        turtle.onkeypress(self.press, key)
        turtle.onkeyrelease(self.release, key)

    def press(self):
        self.down = True

    def release(self):
        self.down = False
a_key = WatchedKey('Up')
b_key = WatchedKey('Left')
a_currently_pressed = a_key.down
b_currently_pressed = b_key.down
def h1():
    tess.up()
    tess.forward(10)


def h2():
    tess.up()
    tess.left(10)


def h3():
    tess.up()
    tess.right(10)


def h4():
    tess.up()
    tess.backward(10)

def h5():
    tess.up()
    tess.left(10)
    tess.forward(10)

while a_currently_pressed and b_currently_pressed:
    h5()
wn.onkeypress(h1, "Up")
wn.onkeypress(h2, "Left")
wn.onkeypress(h3, "Right")
wn.onkeypress(h4, "Down")
wn.listen()
wn.mainloop()
