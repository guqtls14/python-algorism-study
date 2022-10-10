"""
 *packageName    : 
 * fileName       : 42577.전화번호 목록
 * author         : ipeac
 * date           : 2022-10-10
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-10        ipeac       최초 생성
 """
from collections import defaultdict

def solution(phone_book):
    dic = defaultdict(int)
    for pn in phone_book:
        dic[pn] = 1
    for pn in phone_book:
        pn_length = len(pn)
        temp = ""
        for number in pn:
            temp += number
            if temp in dic and temp != pn and pn_length > len(temp):
                return False
    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))
