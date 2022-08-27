"""
 *packageName    : 
 * fileName       : k진수에서 소수 개수 구하기
 * author         : qkrtkdwns3410
 * date           : 2022-08-27
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-27        qkrtkdwns3410       최초 생성
 """
import math


def convert(n, base):
    arr = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return arr[r]
    else:
        return convert(q, base) + arr[r]


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    convert1 = convert(n, k)
    print(f"convert1 : {convert1}")
    s = convert1.split("0")
    print(f"s : {s}")
    for value in s:
        if value == '':
            continue
        if is_prime(int(value)):
            answer += 1
    
    return answer


print(solution(437674, 3))
print(solution(110011, 10))
