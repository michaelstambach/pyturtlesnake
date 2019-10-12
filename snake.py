import turtle

game_height = 400
game_width = 400
speed = 100


def draw_game():
    gamepainter.pu()
    gamepainter.goto(-(game_width/2), -(game_height/2))

    gamepainter.pd()
    gamepainter.width(4)
    gamepainter.forward(game_width)
    gamepainter.seth(90)
    gamepainter.forward(game_height)
    gamepainter.seth(180)
    gamepainter.forward(game_width)
    gamepainter.seth(270)
    gamepainter.forward(game_height)

    screen.update()


def add_segment(turtles, amount = 1):
    for i in range(amount):
        newturtle = turtle.Turtle()
        newturtle.speed(0)  # turn off animations
        newturtle.shape("square")
        newturtle.resizemode("user")
        newturtle.turtlesize(0.5, 0.5)  # resize the square (the original is 20x20px)
        newturtle.pu()

        turtles.append(newturtle)
    return turtles


def right():
    snake[0].seth(0)


def up():
    snake[0].seth(90)


def left():
    snake[0].seth(180)


def down():
    snake[0].seth(270)


def toggle():
    global running
    if running:
        running = False
    elif not running:
        running = True
        screen.ontimer(move, speed)


def check_collision():
    """
    this function returns False if snake[0] is on or out of the game borders or will touch itself in the next frame


    """
    positions = []
    x = round(snake[0].xcor())
    y = round(snake[0].ycor())  # i have to round them because for some reason they deviate a bit sometimes

    for segment in snake:
        positions.append((round(segment.xcor()), round(segment.ycor())))  # same thing here

    if snake[0].heading() == 0:
        if x >= (game_width/2) or (x + 10, y) in positions:
            return False
        else:
            return True

    elif snake[0].heading() == 90:
        if y >= (game_height/2) or (x, y + 10) in positions:
            return False
        else:
            return True

    elif snake[0].heading() == 180:
        if x <= -(game_width / 2) or (x - 10, y) in positions:
            return False
        else:
            return True

    elif snake[0].heading() == 270:
        if y <= -(game_height/2) or (x, y - 10) in positions:
            return False
        else:
            return True

    else:
        return False


def move():
    """
    move the snake forward by looping through a reversed list of the indices of the snake list containing the
    individual segments excluding the 1st one and moving each segment to the one in front of it, except the
    1st one which gets moved 10px forward
    """
    if running and check_collision():
        for i in reversed(range(1, len(snake))):
            snake[i].goto(snake[i-1].xcor(), snake[i-1].ycor())

        snake[0].forward(10)
        screen.update()
        screen.ontimer(move, speed)


def game():
    screen.listen()

    screen.onkey(right, 'Right')
    screen.onkey(up, 'Up')
    screen.onkey(left, 'Left')
    screen.onkey(down, 'Down')
    screen.onkey(toggle, 'space')


snake = []
snake = add_segment(snake, 16)

screen = snake[0].getscreen()
screen.tracer(0)  # im already tracer

gamepainter = turtle.RawTurtle(screen)
gamepainter.speed(0)
gamepainter.hideturtle()


running = False

draw_game()
game()

screen.mainloop()