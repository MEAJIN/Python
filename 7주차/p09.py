count = 1
sum = 0
n = int(input("총합을 구하고 싶은 숫자는:"))
while count <= n:
    sum = sum + count
    count = count + 1
    print("1부터 %s까지의 합계:" % (n),sum)
