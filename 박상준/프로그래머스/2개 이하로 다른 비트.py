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

def convert(n):
    arr = []
    while n // 2:
        arr.append(n % 2)
        n //= 2
    arr.append(n % 2)
    arr.sort(reverse=True)
    arr.insert(0, 0)
    return arr

def solution(numbers):
    answer = []
    for value in numbers:
        con_value = convert(value)
        
        if value % 2 == 0:  # 밸류가 짝수라면
            con_value[-1] =
            pass
        else:  # 밸류가 홀수라면
            pass
    
    return answer

print(solution([2, 7]))  # [3,11]
