"""
 *packageName    : 
 * fileName       : 19637.IF문 좀 대신 써줘(2)
 * author         : ipeac
 * date           : 2022-10-10
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-10        ipeac       최초 생성
 """
# n, m = map(int, input().split())
# 칭호의 개수, 칭호를 출력해야하는 캐릭터들의 개수
import bisect
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
# N개의 줄에 각 칭호의 이름
grade_name = []
grade_score = []
for i in range(n):
    a, b = map(str, input().split())
    grade_name.append(a)
    grade_score.append(int(b))
character_power = []
for i in range(m):
    character_power.append(int(input()))

for value in character_power:
    print(grade_name[bisect.bisect_left(grade_score, value)])
