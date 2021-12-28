from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.colormode(255)
screen.setup(width=500, height=400)
screen.bgcolor((200, 200, 200))
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for i in range(0, len(colors)):
    t = Turtle(shape="turtle")
    t.speed("fastest")
    t.color(colors[i])
    t.penup()
    t.goto(x=-230, y=(-62.5 + 25 * i))
    turtles.append(t)


if user_bet:
    is_race_on = True


while is_race_on:
    for t in turtles:
        if t.xcor() > 210:
            is_race_on = False
            winning_color = t.pencolor()
            if winning_color == user_bet:
                print(f"You've won ! The {winning_color} turtle is the winner !")
            else:

                print(f"You've lost ! The {winning_color} turtle is the winner !")
        rand_distance = random.randint(1, 10)
        t.forward(rand_distance)

screen.exitonclick()