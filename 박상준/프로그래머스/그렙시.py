"""
 *packageName    : 
 * fileName       : 그렙시
 * author         : qkrtkdwns3410
 * date           : 2022-08-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-19        qkrtkdwns3410       최초 생성
 """

import math


def solution(begin, end):
    result = []
    for i in range(begin, end + 1):
        # 1은 문제 조건상 0이므로, 0을 넣어준다.
        if i < 2:
            result.append(0)
            continue
        # 소수 판별하기.
        for j in range(2, int(math.sqrt(i)) + 1):
            # 소수가 아니면, 나눈 몫을 넣어준다
            print("i : %s " % i)
            print("j : %s " % j)
            if i % j == 0:
                result.append(i // j)
                print(i // j)
                print("result : %s " % result)
                print("==========================================")
                break
        else:
            result.append(1)
            print("result : %s " % result)
    return result


solution(1, 10)
print("==========================================")
