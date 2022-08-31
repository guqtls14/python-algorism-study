"""
 *packageName    : 
 * fileName       : 소수 찾기
 * author         : ipeac
 * date           : 2022-08-31
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-31        ipeac       최초 생성
 """
import math
from itertools import permutations

def solution(numbers):
    def is_prime_num(n):
        if n == 0 or n == 1:
            return False
        
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        
        return True
    
    answer = set()
    numbers = list(numbers)
    
    for k in range(1, len(numbers) + 1):
        for i in permutations(numbers, k):
            value2 = ''
            for value in i:
                value2 += value
            if is_prime_num(int(value2)):
                answer.add(int(value2))
    return len(answer)

print(solution("17"))
print(solution("011"))
