"""
 *packageName    : 
 * fileName       : [인턴]수식 최대화
 * author         : qkrtkdwns3410
 * date           : 2022-08-25
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-25        qkrtkdwns3410       최초 생성
 """

# 연산자 우선순위 중복 없음
# 계산된 결과 음수 > 절댓값 변환
# eval 사용불가능할듯
import re
from itertools import permutations


def solution(expression):
    answer = 0
    
    num = re.split('([- | + | *])', expression)
    opr = re.split('[0-9]+', expression)[1:-1]
    
    # 연산자 중복 제거
    opr_permutation = set(opr)
    
    priority_list = []
    
    # 연산의 우선순위  set
    for value in permutations(opr_permutation, len(opr_permutation)):
        priority_list.append(value)
    temp_answer = 0
    
    for priority in priority_list:
        num_copy = num.copy()
        print("==========================================")
        print(f"priority : {priority}")
        for value in priority:
            
            i = 0
            
            while value in num_copy:
                
                if value == num_copy[i]:
                    if value == '*':
                        cal_value = int(num_copy[i - 1]) * int(num_copy[i + 1])
                        num_copy.pop(i - 1)
                        num_copy.pop(i - 1)
                        num_copy.pop(i - 1)
                        
                        num_copy.insert(i - 1, cal_value)
                        i -= 2
                    elif value == '-':
                        cal_value = int(num_copy[i - 1]) - int(num_copy[i + 1])
                        num_copy.pop(i - 1)
                        num_copy.pop(i - 1)
                        num_copy.pop(i - 1)
                        num_copy.insert(i - 1, cal_value)
                        i -= 2
                    
                    elif value == '+':
                        print("+")
                        cal_value = int(num_copy[i - 1]) + int(num_copy[i + 1])
                        num_copy.pop(i - 1)
                        num_copy.pop(i - 1)
                        num_copy.pop(i - 1)
                        num_copy.insert(i - 1, cal_value)
                        i -= 2
                
                if len(num_copy) == 1:
                    print(f"num_copy : {num_copy}")
                    break
                i += 1
        print(f"abs(int(num_copy[0])) : {(int(num_copy[0]))}")
        temp_answer = abs(int(num_copy[0]))
        answer = temp_answer if temp_answer > answer else answer
    
    return answer


# print(solution("100-200*300-500+20"))
print(solution("50+1-4"))  # 1248000
# print(solution(
#     "177-661*999*99-133+221+334+555-166-144-551-166*166-166*166-133*88*55-11*4+55*888*454*12+11-66+444*99"))  # 1248000  # print("==========================================")
# print(solution("50*6-3*2"))
