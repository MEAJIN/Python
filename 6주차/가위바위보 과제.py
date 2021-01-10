import turtle
import random

screen=turtle.Screen()

image1="rock.gif"
image2="scissors.gif"
image3="paper.gif"

screen.addshape(image1)
screen.addshape(image2)
screen.addshape(image3)

game=(["가위","바위","보"])
rsp1=random.choice(game)

s=turtle.textinput("가위 바위 보 선택","가위 바위 보 선택:")
rsp=s


turtle.pensize(70)
t1=turtle.Turtle()



if rsp1=="바위":
   if rsp=="바위":
 
      t1.penup() # 펜을 올려서 그림이 그려지지 않게 함
      t1.shape(image1) # 거북이 모양 설정
      t1.stamp() # 현재 위치에 거북이를 찍는다
      t1.write("당신의 선택",True,"center",("",20))

      t1.goto(200,0) # 200,0 으로 거북이 이동
      t1.shape(image1)
      t1.stamp()
      t1.write("컴퓨터의 선택",True,"center",("",20))
      t1.shape("arrow")
      t1.goto(100,200)
    
      t1.write("비겼습니다", False, "left", ("",30))
 
   elif rsp=="가위":
      t1.penup()
      t1.shape(image2)
      t1.stamp()
      t1.write("당신의 선택",True,"center",("",20))

      t1.goto(200,0)
      t1.shape(image1)
      t1.stamp()
      t1.write("컴퓨터의 선택",True,"center",("",20))
      t1.shape("arrow")
      t1.goto(100,200)
      t1.write("당신이 졌습니다", False, "left", ("",30))
  
   elif rsp=="보":
      t1.penup()
      t1.shape(image3)
      t1.stamp()
      t1.write("당신의 선택",True,"center",("",20))

      t1.goto(200,0)
      t1.shape(image1)
      t1.stamp()
      t1.write("컴퓨터의 선택",True,"center",("",20))
      t1.shape("arrow")
      t1.goto(100,200)
      t1.write("당신이 이겼습니다", False, "left", ("",30))
 

elif rsp1=="가위":
   if rsp=="가위":
      t1.penup()
      t1.shape(image2)
      t1.stamp()
      t1.write("당신의 선택",True,"center",("",20))
  
      t1.goto(200,0)
      t1.shape(image2)
      t1.stamp()
      t1.write("컴퓨터의 선택",True,"center",("",20))
      
      t1.goto(100,200)
      t1.shape("arrow")
      
      t1.write("비겼습니다", False, "left", ("",30))

   elif rsp=="바위":
      t1.penup()
      t1.shape(image1)
      t1.stamp()
      t1.write("당신의 선택",True,"center",("",20))

      t1.goto(200,0)
      t1.shape(image2)
      t1.stamp()
      t1.write("컴퓨터의 선택",True,"center",("",20))
      
      t1.goto(200,200)
      t1.shape("arrow")
      t1.write("당신이 이겼습니다", False, "left", ("",30))

   elif rsp=="보":
      t1.penup()
      t1.shape(image3)
      t1.stamp()
      t1.write("당신의 선택",True,"center",("",20))

      t1.goto(200,0)
      t1.shape(image2)
      t1.stamp()
      t1.write("컴퓨터의 선택",True,"center",("",20))
      
      t1.goto(100,200)
      t1.shape("arrow")
      t1.write("당신이 졌습니다", False, "left", ("",30))

elif  rsp1=="보":
   if rsp=="보":
 
      t1.penup()
      t1.shape(image3)
      t1.stamp()
      t1.write("당신의 선택",True,"center",("",20))

      t1.goto(200,0)
      
      t1.write("컴퓨터의 선택",True,"center",("",20))
      
      
      t1.shape(image3)
      t1.stamp()
      t1.goto(100,200)
      t1.shape("arrow")
      t1.write("비겼습니다", False, "left", ("",30))

   elif rsp=="바위":
      t1.penup()
      t1.shape(image1)
      t1.stamp()
      t1.write("당신의 선택",True,"center",("",20))

      t1.goto(200,0)
      t1.shape(image3)
      t1.stamp()
      t1.write("컴퓨터의 선택",True,"center",("",20))
      t1.shape("arrow")
      t1.goto(100,200)
      
      
      t1.write("당신이 졌습니다", False, "left", ("",30))
  
   elif rsp=="가위":
      t1.penup()
      t1.shape(image2)
      t1.stamp()
      t1.write("당신의 선택",True,"center",("",20))

      t1.goto(200,0)
      t1.shape(image3)
      t1.stamp()
      t1.write("컴퓨터의 선택",True,"center",("",20))
      t1.shape("arrow")
      
      t1.goto(100,200)
      
     
      t1.write("당신이 이겼습니다", False, "left", ("",30))
