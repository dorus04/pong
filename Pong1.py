#pong in python using turtle. Made from tutorial by freecodecamp
import turtle

#setting up window
wn=turtle.Screen()
wn.title("Pong, by Dorus")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#3 items in Pong: 2 paddles, 1 ball
#paddle A
paddle_A = turtle.Turtle()
paddle_A.speed(0) #sets animation speed to the fastest
paddle_A.shape("square") #20x20 by default
paddle_A.color("white")
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.penup() #so paddle doesn't draw a line when moving
paddle_A.goto(-350, 0) #standard position of paddle

#paddle B
paddle_B = turtle.Turtle()
paddle_B.speed(0) #sets animation speed to the fastest
paddle_B.shape("square") #20x20 by default
paddle_B.color("white")
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.penup() #so paddle doesn't draw a line when moving
paddle_B.goto(350, 0) #standard position of paddle

#Ball
ball = turtle.Turtle()
ball.speed(0) #sets animation speed to the fastest
ball.shape("square") #20x20 by default
ball.color("white")
ball.penup() #so paddle doesn't draw a line when moving
ball.goto(0, 0) #standard position of paddle
ball.dx = 0.2
ball.dy = 0.2


#functions for moving paddles
#moving up
def paddle_A_up():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)

def paddle_B_up():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)

#moving down
def paddle_A_down(): 
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)

def paddle_B_down(): 
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)
#keyboard binding
wn.listen()
#controlling paddle A with w, s
wn.onkeypress(paddle_A_up, 'w')
wn.onkeypress(paddle_A_down, 's')
#controlling paddle B with arrows
wn.onkeypress(paddle_B_up, 'Up')
wn.onkeypress(paddle_B_down, 'Down')

#Pen, for writing scores on the screen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
A_score=0
B_score = 0
pen.write('Player A: {}  Player B: {}'.format(A_score, B_score), align='center', font=('Courier', 24, 'normal'))


#Main game loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border checking for collision with top
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    #border checking when it goes off the side, reset to center
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *=-1
        A_score += 1
        pen.clear()
        pen.write('Player A: {}  Player B: {}'.format(A_score, B_score), align='center', font=('Courier', 24, 'normal'))

        

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *=-1
        B_score += 1
        pen.clear()
        pen.write('Player A: {}  Player B: {}'.format(A_score, B_score), align='center', font=('Courier', 24, 'normal'))

    #paddle and ball collision for B
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_B.ycor()+50 and ball.ycor() > paddle_B.ycor()-50):
        ball.dx *= -1
        ball.setx(340)
    #paddle and ball collision for A
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_A.ycor()+50 and ball.ycor() > paddle_A.ycor()-50):
        ball.dx *= -1
        ball.setx(-340)

    
    


