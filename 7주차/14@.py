k=3
for i in range(1,k-1):
   k=int(input("양수 입력(3보다 작으면 종료)"))
   if(k<3):
     print("프로그램을 종료합니다")
     break;
   else:
     check=False

     while True:
        if (k%i)==0:
             print(k,"는 소수가 아니다")
             check==True:
             break;

     if check==False:
      print(k,"는 소수다")
      
    
