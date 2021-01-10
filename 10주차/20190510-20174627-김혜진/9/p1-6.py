heroes = []
heroes.append("아이언맨")
heroes
heroes.append("닥터 스트레인지")
print(heroes)
heroes.append("아이언맨")

num=[1]
num.append(2)
num

list1=[1,2,3]
list1.append(num)
list1

list1.append("아이언맨")
list1

letters = ['A','B','C','D','E','F']

print(letters[0])

print(letters[1])

print(letters[2])

print(letters[0:3])

print(letters[3:])

print(letters[:])

letters = ['a', 'b', 'c', 'd', 'e', 'f']

copy1 = letters

copy1

letters.append('g')

letters

copy1

copy2 = letters[:]

copy2

letters.append('h')

letters

copy2

heroes = ["아이언맨", "토르", "헐크", "스칼렛 위치"]
heroes[1] = "닥터 스트레인지"
print(heroes)

heroes.append("스파이더맨")

print(heroes)

heroes.insert(1, "배트맨")

print(heroes)

heroes.remove("헐크")

print(heroes)

if "배트맨" in heroes:
    heroes.remove("배트맨")

print(heroes)

#
del heroes[0]

print(heroes)
#
last_hero = heroes.pop()

print(last_hero)

print(heroes)
#
heroes = ["아이언맨", "토르", "헐크", "스칼렛 위치"]

print(heroes.index("헐크"))
#
for hero in heroes:
    print(hero)
#
print(heroes)
heroes.sort()
print(heroes)
#
m='파이썬은 정말 쉬운 언어다'
mlist = m.split()
mlist

mlist.sort(key=len)
mlist
#
heroes=["아이언맨", "토르", "헐크", "스칼렛 위치"]
dir(heroes)
#
help(heroes)
