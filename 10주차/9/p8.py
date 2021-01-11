it = {}

it = [{'Name':'홍길동','Tel':'010-1111-0001','Dept':'그린화학과'},
       {'Name':'홍길서','Tel':'010-1111-0002','Dept':'컴퓨터공학과'},
       {'Name':'홍길남','Tel':'010-1111-0003','Dept':'전자공학과'},
       {'Name':'홍길복','Tel':'010-1111-0004','Dept':'바이오생명공학과'}]


print("리스트 데이터")
print(it)
print()

print("전체 학생 이름")
for key in it:
    print(key["Name"],end=" ")

print()
print()

print("전체 학생 명단")
for key in it:
    print(key["Name"], '[전화번호]', key["Tel"],'[학과]',key["Dept"])

print()

print("컴퓨터 공학과 학생 명단")

for key in it:
    if key ["Dept"] == '컴퓨터공학과':
        print(key['Name'])
