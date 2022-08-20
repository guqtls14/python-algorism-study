"""
 *packageName    : 
 * fileName       : 전화번호부
 * author         : ipeac
 * date           : 2022-08-20
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-20        ipeac       최초 생성
 """


def solution(phone_book):
    print("phone_book : %s " % phone_book)
    answer = True
    
    phone_book.sort(key=lambda x: len(x))
    print("phone_book : %s " % phone_book)
    
    for i in range(len(phone_book) - 1):
        for j in range(i + 1, len(phone_book)):
            if phone_book[i] == phone_book[j]:
                answer = False
                print("answer : %s " % answer)
                return answer
            # 전화번호의 길이가 더 김
            if len(phone_book[i]) < len(phone_book[j]):
                if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                    print("phone_book : %s " % phone_book[i])
                    print("phone_book : %s " % phone_book[j])
                    answer = False
                    return answer
    return answer


solution(["119", "97674223", "1195524421"])
print("==========================================")
solution(["123", "456", "789"])
print("==========================================")
solution(["12", "123", "1235", "567", "88"])
