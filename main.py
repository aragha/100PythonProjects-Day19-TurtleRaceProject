# Challenge 3: Create a turtle race/bet game
from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width = 500, height = 400) #keyword parameters fr understanding

colorstr = "red/purple/green/blue/yellow/black/cyan"
colorlist = colorstr.split('/')
# print(colorlist)

user_bet = screen.textinput(title = "Enter your bet - ", prompt = f"Who will win? {colorstr}: ")
winner = ''
turtlelist = []
x = -238
y = -120
xmax = 230
for c in colorlist:
    print(c)
    t = Turtle(shape="turtle")
    t.color(c)
    t.penup()
    t.setpos(x, y)
    turtlelist.append(t)
    y += 50
forwardmove = 0
while winner == '':
    for t in turtlelist:
        # print(t.color()[0])
        if round(t.xcor() > xmax):
            winner = t.color()[0]
        else:
            forwardmove = random.randint(0, 3)
            t.forward(forwardmove)

if winner == user_bet:
    print(f"You won the bet! Your choice {winner} turtle won!!")
else:
    print(f"Sorry your {user_bet} turtle didn't win ({winner} turtle won)")











screen.exitonclick()
