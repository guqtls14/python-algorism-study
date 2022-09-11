"""
 *packageName    : 
 * fileName       : 프로그래머스42579.베스트앨범[해시]
 * author         : qkrtkdwns3410
 * date           : 2022-09-11
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-11        qkrtkdwns3410       최초 생성
 """
from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    dic = defaultdict(list)
    sum_dic = defaultdict(int)
    for i, value in enumerate(zip(genres, plays)):
        dic[value[0]].append([i, value[1]])
        sum_dic[value[0]] = sum_dic[value[0]] + value[1]
    # 장르 플레이 합계 계산
    sum_dic = sorted(list(sum_dic.items()), key=lambda x: -x[1])
    for index in sum_dic:
        tmp = sorted(list(dic[index[0]]), key=lambda x: -x[1])
        cnt = 0
        for value in tmp:
            if cnt == 2:
                break
            answer.append(value[0])
            cnt += 1
        pass
    return answer

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
