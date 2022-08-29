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
    dic = defaultdict()
    for line in record:
        line = list(line.split(" "))
        if line[0] == "Enter" or line[0] == "Change":
            dic[line[1]] = line[2]
    
    print(f"dic : {dic}")
    
    for line in record:
        line = list(line.split(" "))
        if line[0] == "Enter":
            answer.append(dic[line[1]] + "님이 들어왔습니다.")
        elif line[0] == "Leave":
            answer.append(dic[line[1]] + "님이 나갔습니다.")
    
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
