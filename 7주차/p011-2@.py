num1 = 1
while num1 <= 9:
    num2 = 1
    while num2 <= 9:
        print("%d*%d=%d" % (num2,num1,(num1 * num2)),end="\t")
        num2 = num2 + 1
    num1 = num1 + 1
    print()
    

num1 = 1
for num in range(1,10):
    num2 = 1
    for num in range(1,10):
        print("%d*%d=%d" % (num2,num1,(num1 * num2)),end="\t")
        num2 = num2 + 1
    num1 = num1 + 1
    print()
