items = {"커피" : [3000,5,10],
         
         "팬" : [1000,10,20],
         
         "종이컵 ": [20,1050,550],
         
         "우유 ": [500,10,5],
         
         "콜라 ": [1050,22,10]}



keynames = items.keys()


def statusPrint():
    for i in keynames:
        print(i, "\t가격= ", items[i][0],"\t판매량= ", items[i][1], "\t재고= ", items[i][2])

def printKey():
    key = input("판매한 물품은?")
    print()
    print()

    if key in items.sort():
        print(key, "\t가격= ",items[key][0],"\t판매량= ",items[key][1], "\t재고= ",items[key][2])
    else :
        print("판매하지 않는 물품입니다.")
        

    print()
    print()
    printItem(sort)
    

def printItem(sort): #매개변수로 받기

    sell = int(input("판매한 수량은? "))
    print()

    if sell > items[key][2]:
        print("판매한 수량이 재고보다 많습니다. 입력할 수 없습니다.")
        print()
        print()


    elif sell <= items[key][2]:
        items[key][1] = items[key][1] + sell
        items[key][2] = items[key][2] - sell
        print("남은재고는 = ", items[key][2])
        print()

        statusPrint()
        print()


			
def salesFunc():
    printKey()


print()
print()


while True:
    cmd = input("명령을 입력하시오(중지, 출력, 판매): ")
    if cmd == "출력":
        statusPrint()
        print()
        print()

    elif cmd == "판매":
        statusPrint()
        print()
        print()


        while True:
            salesFunc()
            break;


            
    elif cmd == "중지":
        print("재고관리 프로그램을 중지합니다.")
        break;

    

    else:
        print("적합하지 않은 명령입니다.")


            
