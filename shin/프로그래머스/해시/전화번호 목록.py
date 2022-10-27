
# 효율성에서 탈락
# def solution(phone_book):
#     answer=False
#     for i in range(0,len(phone_book)-1):
#         for j in range(i+1,len(phone_book)):
#             if phone_book[i].startswith(phone_book[j]) or phone_book[j].startswith(phone_book[i]):
#                 return False

#     return True

# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)

#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         print(p1,p2)
#         if p2.startswith(p1):
#             return False
#     return True

# phone_book=["119", "97674223", "1195524421"]
# phone_book=["123","456","789"]


def solution(phone_book):
    phone_book.sort()
    for a,b in zip(phone_book,phone_book[1:]):
        if a.startswith(b):
            return False
        elif b.startswith(a):
            return False
    return True
phone_book=["119", "97674223", "1195524421"]
# phone_book=["12","123","1235","567","88"]
print(solution(phone_book))

