"""
 *packageName    : 
 * fileName       : 10157_백준_자리배정_S4
 * author         : ipeac
 * date           : 2022-07-26
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-26        ipeac       최초 생성
 """
# 공연장의 격자 크기 가로 c , 세로r
import sys

c, r = map(int, input().split())
# 관객의 대기 번호 k
k = int(input())

if k > c * r:
    print(0)
    sys.exit(0)

graph = list([0] * c for _ in range(r))
x, y = 0, 0
num = 1
for i in range((c * r) + 1):
    while x < r and graph[x][y] == 0:
        graph[x][y] = num
        if num == k:
            print(y + 1, x + 1)
            exit()
        num += 1
        x += 1
    x -= 1
    y += 1
    while y < c and graph[x][y] == 0:
        graph[x][y] = num
        if num == k:
            print(y + 1, x + 1)
            exit()

        num += 1
        y += 1
    y -= 1
    x -= 1
    while x >= 0 and graph[x][y] == 0:
        graph[x][y] = num
        if num == k:
            print(y + 1, x + 1)
            exit()

        num += 1
        x -= 1
    x += 1
    y -= 1
    while y >= 0 and graph[x][y] == 0:
        graph[x][y] = num
        if num == k:
            print(y + 1, x + 1)
            exit()

        num += 1
        y -= 1
    y += 1
    x += 1
