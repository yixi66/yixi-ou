import turtle
import time
import random


turtle.setup(600, 600)

# snake
snake = turtle.Turtle()
snake.shape("square")
snake.color("pink")
snake.speed(0)
snake.penup()
snake.direction = "stop"


# food
food = turtle.Turtle()
food.shape("circle")
food.color("green")
food.penup()
food.shapesize(0.5)


# snake move
window = turtle.Screen()
window.tracer(0)

def move_up():
    snake.direction = "up"

def move_down():
    snake.direction = "down"

def move_left():
    snake.direction = "left"

def move_right():
    snake.direction = "right"

def move():
    x = snake.xcor()
    y = snake.ycor()
    
    if snake.direction  == "up":
        snake.sety(y+20)
    if snake.direction == "down":
        snake.sety(y-20)

    if snake.direction == "left":
        snake.setx(x-20)
    if snake.direction == "right":
        snake.setx(x+20)


if snake == food:  
    print("snake is long", len(snake))


def random_food_location():
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    food.sety(y)
    food.setx(x)

def check_bounds():
    x = snake.xcor()
    y = snake.ycor()

    if x > 300:
        snake.setx(-300)

    if x < -300:
        snake.setx(300)

    if y > 300:
        snake.sety(-300)

    if y < -300:
        snake.sety(300)

def check_food():
    x_food = food.xcor()
    y_food = food.ycor()
    x = snake.xcor
    y = snake.ycor

# def display_score(score):
#     ref.clear()
#     ref.write(f"score:{score}", font=("arial",18,"italic"))

def check_if_snake_eat_food():
    band = 15
    if food.xcor() <= snake.xcor()+band and food.xcor() >= snake.xcor()-band and food.ycor() <= snake.ycor()+band and food.ycor() >= snake.ycor()-band:
        print(8)
        random_food_location()

window.listen()
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")

snakes_alive = True
score = 0
random_food_location()

while snakes_alive:
    window.update()
    move()
    check_bounds()
    time.sleep(0.2)
    if check_food() == True:
        score += 1
        random_food_location()
        display_score(score)
    check_if_snake_eat_food()
    
    # food_x = food.xcor()
    # print(food_x)
    # food_y = food.ycor()
    # print(food_y)
    # snake_x = snake.xcor()
    # snake_y = snake.ycor()
    # print(snake_x)
    # print(snake_y)


def check_collion():
    x = snake_x
    y = snake_y

    if x == 300:
        return True
    if x == -300:
        return Trueif 
    if y == 300:
        return True
    if y == -300:
        return True

    return False






turtle.mainloop