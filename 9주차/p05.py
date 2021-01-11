import turtle
t = turtle.Turtle()
t.shape("turtle")

def square(x,y,length) : # 한 변의 길이
    t.up()
    t.goto(x,y)
    t.down()
    for i in range(4):
        t.forward(length)
        t.left(90)

square(-200,0,100)
square(0,0,100)
square(200,0,100)
