import turtle
import random, time

game_height = 400
game_width = 400    # please use numbers divisible by 2
speed = 100


def draw_game():
    global screen

    gamepainter = turtle.Turtle()
    gamepainter.speed(8)
    gamepainter.hideturtle()

    gamepainter.pu()
    gamepainter.goto(-(game_width/2), -(game_height/2))

    gamepainter.pd()
    gamepainter.width(5)
    gamepainter.forward(game_width)
    gamepainter.seth(90)
    gamepainter.forward(game_height)
    gamepainter.seth(180)
    gamepainter.forward(game_width)
    gamepainter.seth(270)
    gamepainter.forward(game_height)

    screen = gamepainter.getscreen()


def add_segment(amount=1):
    global snake
    for i in range(amount):
        newturtle = turtle.RawTurtle(screen)
        newturtle.speed(0)  # turn off animations
        newturtle.shape("square")
        newturtle.resizemode("user")
        newturtle.turtlesize(0.5, 0.5)  # resize the square (the original is 20x20px)
        newturtle.pu()

        snake.append(newturtle)


def right():
    if not snake[0].heading() == 180:
        snake[0].seth(0)


def up():
    if not snake[0].heading() == 270:
        snake[0].seth(90)


def left():
    if not snake[0].heading() == 0:
        snake[0].seth(180)


def down():
    if not snake[0].heading() == 90:
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
        if x + 10 >= (game_width/2) or (x + 10, y) in positions:
            return False
        else:
            return True

    elif snake[0].heading() == 90:
        if y + 10 >= (game_height/2) or (x, y + 10) in positions:
            return False
        else:
            return True

    elif snake[0].heading() == 180:
        if x - 10 <= -(game_width / 2) or (x - 10, y) in positions:
            return False
        else:
            return True

    elif snake[0].heading() == 270:
        if y - 10 <= -(game_height/2) or (x, y - 10) in positions:
            return False
        else:
            return True

    else:
        return False


def scored(reset=False):
    """
    this function gets called when the snake touches the target
    it updates the score and resets the target
    """
    global score
    global target_pos

    if reset:
        score = 0
    else:
        score += 1
        add_segment()

    target_x = random.randrange(-(game_width/2) + 10, (game_width/2) - 10, step=10)
    target_y = random.randrange(-(game_height/2) + 10, (game_height/2) - 10, step=10)

    # its a little bit confusing but it works

    target_pos = (target_x,target_y)
    target.goto(target_pos)


def check_target():
    """
    this function checks if the snake is touching the target ("apple")
    """
    snake_pos = (round(snake[0].xcor()), round(snake[0].ycor()))

    if snake_pos == target_pos:
        scored()


def death():
    screen.bgcolor("red")
    screen.update()
    time.sleep(1/4)
    reset_game()

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
        check_target()

        screen.update()
        screen.ontimer(move, speed)

    elif not check_collision():
        death()

        screen.ontimer(move, speed)


def reset_game():
    screen.clear()
    init_game()


def init_game():
    global target, target_pos, snake
    draw_game()

    screen.listen()

    screen.onkey(right, 'Right')
    screen.onkey(up, 'Up')
    screen.onkey(left, 'Left')
    screen.onkey(down, 'Down')
    screen.onkey(toggle, 'space')

    screen.tracer(0)

    target = turtle.RawTurtle(screen)
    target.speed(0)  # turn off animations
    target.shape("square")
    target.resizemode("user")
    target.turtlesize(0.5, 0.5)  # resize the square (the original is 20x20px)
    target.color("red")
    target.pu()
    target_pos = (0, 0)  # storing the targets position in a seperate variable to avoid calling .xcor() and .ycor() every "frame"

    snake = []
    add_segment()

    scored(reset=True)


running = False


init_game()

screen.mainloop()