import random
import turtle

screen=turtle.Screen() # 스크린 선언(*)

image1 = "rock.gif" # 이미지 불러오기
image2 = "scissors.gif"
image3 = "paper.gif"

screen.addshape(image1) # 이미지 추가하기 (이걸 쓰기위해 *을 선언)
screen.addshape(image2)
screen.addshape(image3)

com = (["가위","바위","보"]) # 컴퓨터 선택지
 
comr = random.choice(com) # 컴퓨터가 낸 가위바위보 중 랜덤 선택

rsp = turtle.textinput("가위 바위 보 게임","무엇을 낼건가요?") # 내 선택지
me = rsp # 선택지를 me로 정의

turtle.pensize(5) # 거북이 사이즈
t=turtle.Turtle() # 거북이 생성


if comr=="바위":
   if me=="바위":
 
      t.penup() # 펜을 올려서 그림이 그려지지 않게 함
      t.shape(image1) # 거북이 모양 바위로 설정
      t.stamp() # 현재 위치에 거북이(바위)를 찍는다
      t.write("나",True,"center",("",20)) # 30은 글자 크기
 
      t.goto(200,0) # 200,0 으로 거북이 이동
      t.shape(image1)
      t.stamp()
      t.write("컴퓨터",True,"center",("",20))

      t.shape("turtle")
      t.goto(100,180)
      t.write("비겼습니다", False, "left", ("",30))
 
   
  
   elif me=="보":
      t.penup()
      t.shape(image3)
      t.stamp()
      t.write("나",True,"center",("",20))

      t.goto(200,0)
      t.shape(image1)
      t.stamp()
      t.write("컴퓨터",True,"center",("",20))

      t.goto(100,180)
      t.shape("turtle")
      t.write("나의 승", False, "left", ("",30))


   elif me=="가위":
      t.penup()
      t.shape(image2)
      t.stamp()
      t.write("나",True,"center",("",20))

      t.goto(200,0)
      t.shape(image1)
      t.stamp()
      t.write("컴퓨터",True,"center",("",20))
      
      t.goto(100,180)
      t.shape("turtle")
      t.write("나의 패", False, "left", ("",30))
      

      
elif comr=="가위":
   if me=="가위":
      t.penup()
      t.shape(image2)
      t.stamp()
      t.write("나",True,"center",("",20))
  
      t.goto(200,0)
      t.shape(image2)
      t.stamp()
      t.write("컴퓨터",True,"center",("",20))
      
      t.goto(100,180)
      t.shape("turtle")
      t.write("비겼습니다", False, "left", ("",30))

   elif me=="보":
      t.penup()
      t.shape(image3)
      t.stamp()
      t.write("나",True,"center",("",20))

      t.goto(200,0)
      t.shape(image2)
      t.stamp()
      t.write("컴퓨터",True,"center",("",20))
      
      t.goto(100,180)
      t.shape("turtle")
      t.write("나의 패", False, "left", ("",30))

   elif me=="바위":
      t.penup()
      t.shape(image1)
      t.stamp()
      t.write("나",True,"center",("",20))

      t.goto(200,0)
      t.shape(image2)
      t.stamp()
      t.write("컴퓨터",True,"center",("",20))
      
      t.goto(200,180)
      t.shape("turtle")
      t.write("나의 승", False, "left", ("",30))



elif  comr=="보":
   if me=="보":
 
      t.penup()
      t.shape(image3)
      t.stamp()
      t.write("나",True,"center",("",20))

      t.goto(200,0)
      t.shape(image3)
      t.stamp()
      t.write("컴퓨터",True,"center",("",20))
      
      t.goto(100,180)
      t.shape("turtle")
      t.write("비겼습니다", False, "left", ("",30))
  
   elif me=="가위":
      t.penup()
      t.shape(image2)
      t.stamp()
      t.write("나",True,"center",("",20))

      t.goto(200,0)
      t.shape(image3)
      t.stamp()
      t.write("컴퓨터",True,"center",("",20))
      
      t.shape("turtle")
      t.goto(100,180)
      t.write("나의 승", False, "left", ("",30))

   elif me=="바위":
      t.penup()
      t.shape(image1)
      t.stamp()
      t.write("나",True,"center",("",20))

      t.goto(200,0)
      t.shape(image3)
      t.stamp()
      t.write("컴퓨터",True,"center",("",20))

      t.shape("turtle")
      t.goto(100,180)
      t.write("나의 패", False, "left", ("",30))
