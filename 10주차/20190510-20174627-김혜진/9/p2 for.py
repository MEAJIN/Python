heroes = ['아이언맨', '토르', '헐크', '스칼렛 위치']


def myIndex(sourceList, item):
    
    for i in range (len(sourceList)):
        if item==sourceList[i]:
            
            return i

    return -1

print(myIndex(heroes, '헐크'))
