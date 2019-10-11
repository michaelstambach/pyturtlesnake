import turtle

game_height = 512
game_width = 512
speed = 8

snake = turtle.Turtle()
snake.speed(0)  # turn off animations

screen = snake.getscreen()
gamepainter = turtle.RawTurtle(screen)
gamepainter.speed(0)
gamepainter.hideturtle()


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


def right():
    snake.seth(0)


def up():
    snake.seth(90)


def left():
    snake.seth(180)


def down():
    snake.seth(270)


def toggle():
    global running
    if running:
        running = False
    elif not running:
        running = True
        screen.ontimer(move, 16)


def check_collision():
    """
    this function returns False if the turtle/snake is on or out of the game borders

    it works ok for now but there will need to be a better solution when i implement
    collision with the snake itself
    """
    if snake.heading() == 0:
        if snake.xcor() >= (game_width/2):
            return False
        else:
            return True

    elif snake.heading() == 90:
        if snake.ycor() >= (game_height/2):
            return False
        else:
            return True

    elif snake.heading() == 180:
        if snake.xcor() <= -(game_width / 2):
            return False
        else:
            return True

    elif snake.heading() == 270:
        if snake.ycor() <= -(game_height/2):
            return False
        else:
            return True

    else:
        return False


def move():
    if running and check_collision():
        snake.forward(speed)
        screen.ontimer(move, 16)


def game():
    screen.listen()

    screen.onkey(right, 'Right')
    screen.onkey(up, 'Up')
    screen.onkey(left, 'Left')
    screen.onkey(down, 'Down')
    screen.onkey(toggle, 'space')


running = False

draw_game()
game()

screen.mainloop()