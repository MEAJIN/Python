numbers = [11,33,55,39,21,25,9,41,13,2]

for num in numbers:
    if(num % 2) == 0:
        print('리스트는 짝수를 포함합니다.')
        break
else:
    print('리스트에는 짝수가 없습니다.')



print()

numbers = [11,33,55,39,21,25,9,41,13]

i = 0
while (i < len(numbers)):
    if (numbers[i] % 2) == 0 :
        print("리스트는 짝수를 포함합니다.")
        break;
    
    else:
        print('리스트에는 짝수가 없습니다.')
    i += 1
