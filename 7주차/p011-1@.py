dan = 2
while dan <= 9:
    num = 1
    while num <=9:
        print("%d*%d=%d" % (dan,num,(dan * num)))
        num = num+1
    dan = dan + 1
    print()



for dan in range(2,10):
    num = 1
    for num in range(1,10):
        print("%d*%d=%d" % (dan,num,(dan * num)))
        num = num+1
        
    print()
