n=int(input("정수를 입력하시오.:"))

fact=1

for i in range(1,n+1):
    fact=fact * i

print(n,"!은", fact, "이다.")


n=int(input("정수를 입력하시오.:"))

fact=1

a=0
i=1
while a < n:
    fact=fact*i
    i+=1
    a+=1
print(n,"!은", fact, "이다.")

