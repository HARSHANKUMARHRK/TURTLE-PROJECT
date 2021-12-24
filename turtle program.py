import turtle, random
screen = turtle.Screen()
screen.setup(500,350)
screen.bgcolor("lightyellow")
finish = turtle.Turtle()
finish.penup()
finish.goto(155, 120)
finish.pendown()
finish.right(90)
finish.forward(180)
tred = turtle.Turtle()
tred.shape("turtle")
tred.color("red")
tred.penup()
tred.goto(-160, -10)
tred.pendown()
tblue = turtle.Turtle()
tblue.shape("turtle")
tblue.color("blue")
tblue.penup()
tblue.goto(-160, 30)
tblue.pendown()
tgreen = turtle.Turtle()
tgreen.shape("turtle")
tgreen.color ("green")
tgreen.penup()
tgreen.goto(-160,70)
tgreen.pendown()

turtlelist = [tred, tblue, tgreen] 
run = 0
 
while run == 0:
 turtle = random.choice(turtlelist)
 turtle.forward(random.randint(1,5))
 if turtle.xcor() >= 155:
  turtle.color("yellow")
  run = 1
  print (" won ")     