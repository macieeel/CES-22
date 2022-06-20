import turtle    # Tess becomes a traffic light.

wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
wn.title("Lista 02 -  Exercício 01")   # define o título da janela
width = 1


def change_to_red():
    tess.pencolor("red")
    tess.color("red")


def change_to_blue():
    tess.pencolor("blue")
    tess.color("blue")


def change_to_green():
    tess.pencolor("green")
    tess.color("green")


def increase_width():
    global width
    if width < 20:
        width += 1
    tess.pensize(width)


def decrease_width():
    global width
    if width > 1:
        width -= 1
    tess.pensize(width)


def go_forward():
    tess.forward(20)


def go_back():
    tess.backward(20)


def turn_right():
    tess.right(90)
    # tess.forward(10)


def turn_left():
    tess.left(90)
    # tess.forward(10)


state = 1


def change_bg_color():
    global state
    if state == 1:
        wn.bgcolor("white")
        state = 2
    elif state == 2:
        wn.bgcolor("gray")
        state = 3
    elif state == 3:
        wn.bgcolor("lightgreen")
        state = 1


penUp = 0


def change_pen_mode():
    global penUp
    if penUp == 1:
        tess.pendown()
        penUp = 0
    else:
        tess.penup()
        penUp = 1


wn.onkey(change_to_red, "r")
wn.onkey(change_to_green, "g")
wn.onkey(change_to_blue, "b")
wn.onkey(increase_width, "+")
wn.onkey(decrease_width, "-")
wn.onkey(go_forward, 'w')
wn.onkey(go_back, 's')
wn.onkey(turn_right, 'd')
wn.onkey(turn_left, 'a')
wn.onkey(change_bg_color, "t")
wn.onkey(change_pen_mode, "p")


wn.listen()     # Listen for events
wn.mainloop()
