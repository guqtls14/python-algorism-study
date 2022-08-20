"""
 *packageName    : 
 * fileName       : Lv2.사람나열
 * author         : ipeac
 * date           : 2022-08-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-18        ipeac       최초 생성
 """
import itertools
import math


def solution(n, k):
    answer = [value for value in range(1, n + 1)]
    result = []
    while n != 0:
        temp = math.factorial(n - 1)
        print("temp : %s " % temp)
        index = (k - 1) // temp
        print("index : %s " % index)
        k = k % temp
        print("k : %s " % k)
        result.append(answer.pop(index))
        n -= 1
        print("result : %s " % result)
    
    return answer


solution(3, 5)
