"""
 *packageName    : 
 * fileName       : 14889.스타트와 링크
 * author         : qkrtkdwns3410
 * date           : 2022-09-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-18        qkrtkdwns3410       최초 생성
 """

import math
import sys
from itertools import combinations

input = sys.stdin.readline
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
p = [i for i in range(n)]

answer = math.inf

def calc(start):
    global answer
    link = []
    # 링크에는 스타트에 없는 숫자를 집어넣는다.
    for i in p:
        if i not in start:
            link.append(i)
    sum, sum2 = 0, 0
    for i in range(n // 2):
        for j in range(n // 2):
            if i == j: continue
            sum += a[start[i]][start[j]]
            sum2 += a[link[i]][link[j]]
    diff = abs(sum - sum2)
    answer = answer if answer < diff else diff

for i in combinations(p, n // 2):
    calc(i)
print(answer)
