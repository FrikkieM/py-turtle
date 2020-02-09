#Complicated Hello World

import turtle

tt = turtle.Turtle()
tt.shape('arrow')
tt.color('white')
wn = turtle.Screen()

tt.penup()
tt.goto(-300,0)

size = 8

#Initialize the Screen
wn.bgcolor("black")

#H
def drawH(ttpen):    
    ttpen.pendown()
    ttpen.left(90)
    ttpen.forward(size * 10)
    ttpen.back(size * 20)
    ttpen.penup()
    ttpen.forward(size * 10)
    ttpen.right(90)
    ttpen.pendown()
    ttpen.forward(size * 5)
    ttpen.left(90)
    ttpen.forward(size * 10)
    ttpen.back(size * 20)
    ttpen.penup()
    ttpen.forward(size * 10)
    ttpen.right(90)
    ttpen.penup()
    ttpen.forward(size * 2)

#E
def drawE(ttpen):
    ttpen.pendown()
    ttpen.left(90)
    ttpen.forward(size * 10)
    ttpen.right(90)
    ttpen.forward(size * 4)
    ttpen.back(size * 4)
    ttpen.right(90)
    ttpen.forward(size * 20)
    ttpen.left(90)
    ttpen.forward(size * 4)
    ttpen.back(size * 4)
    ttpen.left(90)
    ttpen.penup()
    ttpen.forward(size * 10)
    ttpen.right(90)
    ttpen.pendown()
    ttpen.forward(size * 2.8)
    ttpen.penup()
    ttpen.forward(size * 2.2)


#L
def drawL(ttpen):
    ttpen.left(90)
    ttpen.forward(size * 10)
    ttpen.left(180)
    ttpen.pendown()
    ttpen.forward(size * 20)
    ttpen.left(90)
    ttpen.forward(size * 4)
    ttpen.penup()
    ttpen.back(size * 4)
    ttpen.left(90)
    ttpen.forward(size * 10)
    ttpen.right(90)
    ttpen.forward(size * 6)

#O
def drawO(ttpen):        
    ttpen.right(90)
    ttpen.pendown()
    ttpen.forward(size * 10)
    ttpen.left(90)
    ttpen.forward(size * 4)
    ttpen.left(90)
    ttpen.forward(size * 20)
    ttpen.left(90)
    ttpen.forward(size * 4)
    ttpen.left(90)
    ttpen.forward(size * 10)
    ttpen.penup()
    ttpen.left(90)
    ttpen.forward(size * 6)

#W
def drawW(ttpen):
    ttpen.left(90)
    ttpen.forward(size * 10)
    ttpen.left(180)
    ttpen.pendown()
    ttpen.forward(size * 20)
    ttpen.left(90)
    ttpen.forward(size * 4)
    ttpen.left(90)
    ttpen.forward(size * 20)
    ttpen.left(180)
    ttpen.forward(size * 20)
    ttpen.left(90)
    ttpen.forward(size * 4)
    ttpen.left(90)
    ttpen.forward(size * 20)
    ttpen.penup()
    ttpen.back(size * 10)
    ttpen.right(90)
    ttpen.forward(size * 2)

#W
def drawR(ttpen):
    ttpen.right(90)
    ttpen.forward(size * 10)
    ttpen.left(180)
    ttpen.pendown()
    ttpen.forward(size * 20)
    ttpen.right(90)
    ttpen.forward(size * 5)
    ttpen.right(90)
    ttpen.forward(size * 8)
    ttpen.right(90)
    ttpen.forward(size * 5)
    ttpen.back(size * 4)
    ttpen.left(90)
    ttpen.forward(size * 12)
    ttpen.penup()
    ttpen.back(size * 10)
    ttpen.left(90)
    ttpen.forward(size * 2.4)

#D
def drawD(ttpen):
    ttpen.forward(size * 4)
    ttpen.left(90)
    ttpen.forward(size * 10)
    ttpen.left(180)
    ttpen.pendown()
    ttpen.forward(size * 20)
    ttpen.right(90)
    ttpen.forward(size * 5)
    ttpen.right(90)
    ttpen.forward(size * 12)
    ttpen.right(90)
    ttpen.forward(size * 5)
    ttpen.penup()
    ttpen.forward(size * 2)
    



def space(ttpen):
    ttpen.penup()
    ttpen.forward(size * 8)


drawH(tt)
drawE(tt)
drawL(tt)
drawL(tt)
drawO(tt)

space(tt)

drawW(tt)
drawO(tt)
drawR(tt)
drawL(tt)
drawD(tt)

tt.goto(0,0)
tt.goto(0,200)
