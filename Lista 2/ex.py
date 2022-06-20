import turtle

# turtle.setup(500, 500)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Lista 02")   # define o título da janela
alex = turtle.Turtle()   # alex will become a traffic light
tess = turtle.Turtle()   # tess will be able to move listening to keyboard events


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    alex.pensize(3)
    alex.color("black", "darkgrey")
    alex.begin_fill()
    alex.forward(80)
    alex.left(90)
    alex.forward(200)
    alex.circle(40, 180)
    alex.forward(200)
    alex.left(90)
    alex.end_fill()


draw_housing()

alex.penup()
# Position alex onto the place where the green light should be
alex.forward(40)
alex.left(90)
alex.forward(50)
# Turn alex into a big green circle
alex.shape("circle")
alex.shapesize(3)
alex.fillcolor("green")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change alex' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0


def advance_state_machine_timer():
    global state_num
    if state_num == 0:    # Transition from state 0 to state 1
        alex.forward(70)
        alex.fillcolor("orange")
        state_num = 1
    elif state_num == 1:    # Transition from state 1 to state 2
        alex.forward(70)
        alex.fillcolor("red")
        state_num = 2
    else:  # Transition from state 2 to state 0
        alex.back(140)
        alex.fillcolor("green")
        state_num = 0

    wn.ontimer(advance_state_machine_timer, 2000)


wn.ontimer(advance_state_machine_timer, 2000)


# Here are the functions that will change Tess' properties
def change_to_red():
    tess.pencolor("red")
    tess.color("red")


def change_to_blue():
    tess.pencolor("blue")
    tess.color("blue")


def change_to_green():
    tess.pencolor("green")
    tess.color("green")


# This variable holds the current width value
width = 1


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


penUp = 0


def change_pen_mode():
    global penUp
    if penUp == 1:
        tess.pendown()
        penUp = 0
    else:
        tess.penup()
        penUp = 1


# This variable holds the current state of background color
bg_color = 1


# This funtion change the background color according with it's state
def change_bg_color():
    global bg_color
    if bg_color == 1:
        wn.bgcolor("white")
        bg_color = 2
    elif bg_color == 2:
        wn.bgcolor("lightblue")
        bg_color = 3
    elif bg_color == 3:
        wn.bgcolor("lightgreen")
        bg_color = 1


# Bind the events handlers to the keys we want
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
