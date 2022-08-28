"""
 *packageName    :
 * fileName       : 오픈채팅방
 * author         : qkrtkdwns3410
 * date           : 2022-08-28
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-28        qkrtkdwns3410       최초 생성
 """
from collections import defaultdict


def solution(record):
    answer = []
    print(f"record : {record}")
    dic = defaultdict()
    for line in record:
        line = list(line.split(" "))
        if line[0] == "ENTER":
    
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
