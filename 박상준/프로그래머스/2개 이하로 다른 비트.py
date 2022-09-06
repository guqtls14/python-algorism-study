"""
 *packageName    : 
 * fileName       : 2개 이하로 다른 빝트
 * author         : qkrtkdwns3410
 * date           : 2022-09-04
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-04        qkrtkdwns3410       최초 생성
 """

def solution(numbers):
    answer = []
    
    for number in numbers:
        
        if number % 2 == 0:  # 숫자가 짝수인 경우 맨 마지막 숫자 는 0
            answer.append(number + 1)
        else:  # 숫자가 홀수 인 경우
            number = '0' + bin(number)[2:]
            number = number[:number.rindex('0')] + '10' + number[number.rindex('0') + 2:]
            answer.append(int('0b' + number, 2))
    
    return answer

print(solution([2, 7]))  # [3,11]
