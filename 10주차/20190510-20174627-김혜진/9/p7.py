phone_book = {}

phone_book = { "김혜진":"010-1111-2222"}

print(phone_book)

phone_book["강감찬"] = "010-5555-4444"
phone_book["김김찬"] = "010-5555-9999"

print(phone_book["강감찬"])

print(phone_book.keys())

print(phone_book.values())

for key in phone_book.keys():
    print(key)

for key in phone_book.keys():
    print(key, phone_book[key])

del phone_book["강감찬"]

print(phone_book)

phone_book.clear()

print(phone_book)

dict={'name':'홍길동','age':7,'class':'초급'}

print(dict['name'])

print(dict['age'])

