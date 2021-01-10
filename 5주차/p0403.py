import turtle
t=turtle.Turtle()
t.shape("turtle")

a=turtle.textinput("터틀인사!!!","첫번째 사람의 이름을 입력하시오: ")
b=turtle.textinput("터틀인사!!!","두번째 사람의 이름을 입력하시오: ")

t.write("안녕하세요? %s, %s씨, 터틀 인사드립니다." %(a,b))

t.left(90)
t.forward(100)

t.left(90)
t.forward(20)
t.write("안녕하세요? %s씨, 터틀 인사드립니다." %a)

t.forward(80)
t.left(90)


t.forward(20)
t.write("안녕하세요? %s씨, 터틀 인사드립니다." %b)

t.forward(60)
t.write(" %s, %s씨, 그럼 이만." %(a,b))

t.forward(20)

t.left(90)
t.forward(100)
