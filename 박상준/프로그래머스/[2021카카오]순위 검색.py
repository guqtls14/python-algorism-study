"""
 *packageName    : 
 * fileName       : [2021카카오]순위 검색
 * author         : qkrtkdwns3410
 * date           : 2022-08-24
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-24        qkrtkdwns3410       최초 생성
 """
import bisect
from collections import defaultdict
from itertools import combinations as cb


def solution(info, query):
    query = [i.replace('and', '').split() for i in query]
    info = [i.split() for i in info]
    
    info_dic = defaultdict(list)
    
    for lang, job, career, food, score in info:
        for i in range(5):
            for j in cb([lang, job, career, food], i):
                info_dic[''.join(j)].append(int(score))
    for i in info_dic:
        info_dic[i].sort()
    answer = []
    for i in query:
        score = int(i[-1])
        result = ''.join(i[:-1]).replace('-', '')
        print(f"result : {result}")
        s = info_dic[result]
        answer.append(len(s) - bisect.bisect_left(s, score))  # 더 작은 친구의 개수를 빼준다.
    return answer


solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260",
          "java backend junior chicken 80", "python backend senior chicken 50"],
         ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250",
          "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"])
