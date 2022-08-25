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
    print(f"opr : {opr}")
    
    # 연산자 중복 제거
    opr_permutation = set(opr)
    
    priority_list = []
    
    # 연산의 우선순위  set
    for value in permutations(opr_permutation, len(opr_permutation)):
        priority_list.append(value)
    print(f"priority_list : {priority_list}")
    
    for priority in priority_list:
        temp_answer = 0
        num_copy = num.copy()
        
        for value in priority:
            for i, number in enumerate(num_copy):
                print(f"number : {number}")
                
                if value == number:
                    
                    if value == '*':
                        cal_value = int(num_copy[i - 1]) * int(num_copy[i + 1])
                        num_copy.pop(i - 1)
                        num_copy.pop(i - 1)
                        num_copy.pop(i - 1)
                        
                        temp_answer += cal_value
                        num_copy.insert(i - 1, cal_value)
                    elif value == '-':
                        cal_value = int(num_copy[i - 1]) - int(num_copy[i + 1])
                        num_copy.pop(i - 1)
                        num_copy.pop(i - 1)
                        num_copy.pop(i - 1)
                        temp_answer += cal_value
                        num_copy.insert(i - 1, cal_value)
                    
                    elif value == '+':
                        cal_value = int(num_copy[i - 1]) + int(num_copy[i + 1])
                        num_copy.pop(i - 1)
                        num_copy.pop(i - 1)
                        num_copy.pop(i - 1)
                        temp_answer += cal_value
                        num_copy.insert(i - 1, cal_value)
        
        temp_answer = abs(temp_answer)
        print(f"temp_answer : {temp_answer}")
        answer = temp_answer if temp_answer > answer else answer
    
    return answer


print(solution("100-200*300-500+20"))
print("==========================================")
print(solution("50*6-3*2"))
