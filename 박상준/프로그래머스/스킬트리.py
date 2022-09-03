"""
 *packageName    : 
 * fileName       : 스킬트리
 * author         : ipeac
 * date           : 2022-09-03
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-03        ipeac       최초 생성
 """

# skill  : 선행스킬 # skill_trees : 유저들이 만든 스킬트리를 담은 배열
# 가능한 스킬트리 수 반환
def solution(skill, skill_trees):
    answer = 0
    
    for skills in skill_trees:
        flag = True
        skill_list = list(skill)
        
        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    flag = False
                    break
        if flag:
            answer += 1
    
    return answer

# print(solution("CBD", ["BACDE"]))
print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
