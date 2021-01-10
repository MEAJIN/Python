import random

tries = 0
guess = 0
answer = random.randint(1,100)
print(answer)

print("1부터 100 사이의 숫자를 맞추시오")

while guess != answer:
    guess = int(input("숫자를 입력하시오:"))
    tries = tries + 1
    if guess < answer:
        print("답보다 낮음!")
    elif guess > answer:
        print("답보다 높음!")

if guess == answer:
    print("축하합니다. 시도횟수=",tries)


import random
tries=0
guess=0
answer=random.randint(1,100)
print(answer)
print("1부터 100사이의 숫자를 맞추시오")

for i in range(1,100):
  if(answer!=guess):
    guess=int(input("숫자를 입력하시오"))
    tries=tries+1
    if guess<answer:
        print("정답보다 작습니다")
        
    elif guess>answer:
        print("정답보다 큽니다")
        

if guess==answer:
    print("축하합니다. 시도횟수=",tries)
