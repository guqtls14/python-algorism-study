"""
 *packageName    : 
 * fileName       : lv1.철자 분리 집합
 * author         : ipeac
 * date           : 2022-10-10
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-10        ipeac       최초 생성
 """
from collections import Counter, deque

n = int(input())
s = input()
count = 0
if len(s) == 1:
    print(1)
    exit()
else:
    for i in range(1, n):
        if s[i - 1] == s[i]:
            continue
        else:
            count += 1
print(count + 1)
