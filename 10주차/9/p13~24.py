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
