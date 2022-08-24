"""
 *packageName    : 
 * fileName       : [2019카카오]튜플
 * author         : qkrtkdwns3410
 * date           : 2022-08-24
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-24        qkrtkdwns3410       최초 생성
 """


def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key=lambda x: len(x))
    print(f"s : {s}")
    answer = []
    for i in s:
        words = i.split(",")
        print(f"words : {words}")
        for word in words:
            if int(word) not in answer:
                answer.append(int(word))
    
    return answer


solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")
