"""
 *packageName    : 
 * fileName       : 19637.IF문 좀 대신 써줘
 * author         : ipeac
 * date           : 2022-10-07
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-07        ipeac       최초 생성
 """
import bisect

n, m = map(int, input().split())
name = []
score_list = []
for i in range(n):
    title, score, = map(str, input().split())
    name.append(title)
    score_list.append(int(score))

power = [0, 9999, 10000, 10001, 50000, 100000, 500000, 1000000]
power.sort()

for value in power:
    print(name[bisect.bisect_left(score_list, value)])
