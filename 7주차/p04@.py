import turtle
t = turtle.Turtle()
t.shape("turtle")

#정삼각형 그리기

for i in range(3):
    t.forward(100)
    t.left(360/3)

# 이동하기

t.penup()
t.goto(200,0)
t.pendown()

# 정사각형 그리기

for i in range(4):
    t.forward(100)
    t.left(360/4)
#######################
t.penup()
t.goto(300,300)
t.pendown()
  
#정삼각형 그리기
a=0
while a<3:
    t.forward(100)
    t.left(360/3)
    a = a +1

# 이동하기

t.penup()
t.goto(400,0)
t.pendown()

# 정사각형 그리기
a=0
while a<4:
    t.forward(100)
    t.left(360/4)
    a=a+1
