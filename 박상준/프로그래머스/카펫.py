"""
 *packageName    : 
 * fileName       : 카펫
 * author         : ipeac
 * date           : 2022-09-04
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-04        ipeac       최초 생성
 """

def num_div(n):
    arr = []
    for i in range(1, n + 1):
        if n % i == 0:
            arr.append(i)
    if len(arr) % 2 != 0:
        arr.insert(len(arr) // 2 + 1, arr[len(arr) // 2])
    return arr

def solution(brown, yellow):
    answer = []
    arr = num_div(yellow)
    for i in range(len(arr) // 2):
        num1, num2 = arr[i], arr[(len(arr) - 1) - i]
        num3, num4 = num1 + 2, num2 + 2
        if brown == num3 * num4 - (num1 * num2):
            answer.extend([num4, num3])
            return answer
    
    return answer

print(solution(12, 4))
# print(solution(8, 1))
# print(solution(24, 24))
