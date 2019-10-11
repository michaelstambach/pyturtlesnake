import turtle


snake = turtle.Turtle()
screen = snake.getscreen()
snake.speed(0) # turn off animations


def right():
    snake.setheading(0)


def up():
    snake.setheading(90)


def left():
    snake.setheading(180)


def down():
    snake.setheading(270)


def toggle():
    global running
    if running:
        running = False
    elif not running:
        running = True
        screen.ontimer(move, 16)


def move():
    if running:
        snake.forward(8)
        screen.ontimer(move, 16)


screen.listen()

screen.onkey(right, 'Right')
screen.onkey(up, 'Up')
screen.onkey(left, 'Left')
screen.onkey(down, 'Down')
screen.onkey(toggle, 'space')

running = False

screen.mainloop()