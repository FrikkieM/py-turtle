#Turtle Pong Game
#Followed Tutorial By @TokyoEdTech
#Tutorial found at https://www.youtube.com/watch?v=C6jJg9Zan7w
#Added some of my own stuff and used winsound's Beep function to generate audio

import turtle
import winsound

#Variables
gameSpeed = 0.17
scoreA = 0
scoreB = 0

wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)        #Allows us to update the screen manually, for better speed


#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)   #sets animation speed to max
paddle_a.shape("square")  #Draws 20px by 20px shape
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)    #stretches width, default height
paddle_a.penup()    #Prevents drawing line
paddle_a.goto(-350,0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)   #sets animation speed to max
paddle_b.shape("square")  #Draws 20px by 20px shape
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)    #stretches width, default height
paddle_b.penup()    #Prevents drawing line
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)   #sets animation speed to max
ball.shape("square")  #Draws 20px by 20px shape
ball.color("white")
ball.penup()    #Prevents drawing line
ball.goto(0,0)
ball.dx = gameSpeed   #Delta x / Moves by 2 everytime it moves
ball.dy = gameSpeed

#Pen for Scoring
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
    
def updateScore():
    pen.clear()
    pen.write(f"Player A: {scoreA}  Player B: {scoreB}", align="center", font=("Courier",14,"bold"))

updateScore()

def playSound():
    #https://docs.python.org/3.7/library/winsound.html
    winsound.PlaySound(winsound.Beep(400,100),winsound.SND_ASYNC)

#Functions to move the paddles
def paddle_a_up():
    y = paddle_a.ycor() #return y coord
    y += 30
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() #return y coord
    y -= 30
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() #return y coord
    y += 30
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() #return y coord
    y -= 30
    paddle_b.sety(y)


#Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#Main Game Loop
while True:
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        #ball.setx(390)
        ball.goto(0,0)
        ball.dx *= -1
        scoreA += 1
        updateScore()

    if ball.xcor() < -390:
        #ball.setx(-390)
        ball.goto(0,0)
        ball.dx *= -1
        scoreB += 1
        updateScore()

        
    #Paddle B and Ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and ((ball.ycor() < paddle_b.ycor()+40) and (ball.ycor() > paddle_b.ycor()-40)):
        ball.setx(340)
        playSound()
        ball.dx *= -1
    #Paddle A and Ball collisions
    if (ball.xcor() < -340 and ball.xcor() > -350) and ((ball.ycor() < paddle_a.ycor()+40) and (ball.ycor() > paddle_a.ycor()-40)):
        ball.setx(-340)
        playSound()
        ball.dx *= -1

        
    wn.update() #Updates the screen
