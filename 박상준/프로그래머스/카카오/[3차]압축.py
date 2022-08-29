"""
 *packageName    : 
 * fileName       : [3차]압축
 * author         : qkrtkdwns3410
 * date           : 2022-08-26
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-26        qkrtkdwns3410       최초 생성
 """
from collections import defaultdict


def solution(msg):
    answer = []
    
    # map 에 영문 대문자 색인 처리
    word_indexing = [chr(value) for value in range(65, 91)]
    dic = defaultdict(int)
    i = 1
    for value in word_indexing:
        dic[value] = i
        i += 1
    print(f"dic : {dic}")
    cnt = 27
    search = ''
    
    i = 0
    while i < len(msg):
        search += msg[i]
        print(f"search : {search}")
        if search in dic:
            i += 1
            continue
        elif search not in dic:
            dic[search] = cnt
            
            cnt += 1
            print(f"dic : {dic}")
            
            answer.append(dic[search[:-1]])
            
            search = ''
    
    answer.append(dic[search])
    return answer


print(solution("KAKAO"))
