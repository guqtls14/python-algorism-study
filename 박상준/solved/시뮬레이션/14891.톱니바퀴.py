"""
 *packageName    : 
 * fileName       : 14891.톱니바퀴
 * author         : ipeac
 * date           : 2022-10-15
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-15        ipeac       최초 생성
 """
"""
12시 방향부터 시계방향 순서대로 주어진다.
n 극 0
s 극 1
"""
from collections import deque

def rotate_right(x, d):
    # x 값이 4 초과 or 이전 기어의 오른쪽 축 == 지금 기어의 왼쪽 축이 같으면 작동 x
    if x > 4 or gears[x - 1][2] == gears[x][-2]:
        return
    # 기준점 기어 오른 축 != 오른 기어의 왼축
    if gears[x - 1][2] != gears[x][-2]:
        # 다음 기어 탐색 > 축이 다르기에 로테이트 반대로함
        rotate_right(x + 1, -d)
        # 지금 기어를 d로 로테이트함
        gears[x].rotate(d)

def rotate_left(x, d):
    if x < 1 or gears[x + 1][-2] == gears[x][2]:
        return
    if gears[x + 1][-2] != gears[x][2]:
        rotate_left(x - 1, -d)
        gears[x].rotate(d)

gears = {}
for i in range(1, 5):
    gears[i] = deque((map(int, input())))

for _ in range(int(input())):
    x, d = map(int, input().split())
    
    rotate_right(x + 1, -d)
    rotate_left(x - 1, -d)
    gears[x].rotate(d)

ans = 0
for i in range(4):
    ans += gears[i + 1][0] * (2 ** i)

print(ans)
