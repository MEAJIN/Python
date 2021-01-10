from datetime import datetime

d=datetime.now()
print("올해의 년도:",str(d.year))

year=int(input("출생년도는?"))
age=(d.year-year)

if age>=15:
    print("올해 %s살(만 나이) 이군요. 이 영화를 보실 수 있습니다."% age)

else:
    print("올해 %s살(만 나이) 이군요. 이 영화를 보실 수 없습니다."% age)
