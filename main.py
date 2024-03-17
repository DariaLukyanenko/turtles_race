from turtle import Turtle, Screen
import random

all_turtles = []
race_on = True
TURTLES_COLORS = ['red','yellow','orange','pink','green','blue']
WIDTH, HEIGHT = 700, 500
x=0
def game_init():
    for i in range(0,5):
        turtle = Turtle()
        turtle.color(TURTLES_COLORS[i])
        turtle.penup()
        turtle.setpos(0,random.randint(-HEIGHT/4,HEIGHT/4))
        all_turtles.append(turtle)

screen = Screen()
screen.setup(WIDTH,HEIGHT)
bet=screen.textinput(title='Make your bet', prompt='Write on which turtle you will bet')

#TODO Use user's choice to implement bet mechanics 

def game():
    global race_on
    game_init()
    while race_on:
        for i in all_turtles:
            i.fd(random.randint(1,30))
            print(i.xcor())
            if i.xcor()>320:
                race_on = False
                print(i.pencolor())
                print(bet)
                if i.pencolor()==bet:
                    print("you win")
                else:
                    print('you lose')
game()

screen.exitonclick()