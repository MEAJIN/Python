import turtle

t=turtle.Turtle() # 화살표 생성
t.shape("turtle") # 화살표를 거북이로 바꿈

s = turtle.textinput("", "몇각형을 원하시나요?")

n = int(s)

for i in range(n):
    t.forward(100)
    t.left(360/n)

t=turtle.Turtle() # 화살표 생성
t.shape("turtle") # 화살표를 거북이로 바꿈

a = turtle.textinput("", "몇각형을 원하시나요?")

b = int(a)
i=0
while i < b:
    t.forward(100)
    t.left(360/b)
    i+=1
    
