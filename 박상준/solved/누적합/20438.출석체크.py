"""
 *packageName    : 
 * fileName       : 20438.출석체크
 * author         : ipeac
 * date           : 2022-10-07
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-07        ipeac       최초 생성
 """
import itertools

# n 학생의 수 ; k 졸고있는 학생의 수;  q 지환이가 출석코드를 보낼 학생의 수 ; m 주어질 구간의 수
n, k, q, m = map(int, input().split())

student = [0] * (n + 3)
check = [0] * (n + 3)

# 졸고있는 학생
sleep = list(map(int, input().split()))
for s in sleep:
    student[s] = 1

# q 명의 출석 코드를 받을 학생의 입장 번호
# 해당 학생은 본인의 입장 번호의 배수인 학생들에게 출석 코드를 보내어 해당 강의의 출석을 할 수 있게끔 한다.
code = list(map(int, input().split()))
for c in code:
    if student[c] == 1:
        continue
    for j in range(c, n + 3, c):
        if not student[j]:
            check[j] = 1
# m개의 줄동안 범위 s, e 가 공백을 사이에 두고 주어진다.
# 해당 범위 안에서 출석이 되지 않은 학생들의 수를 구함
#
#
# 부분합을 구합니다.
part_sum = list(itertools.accumulate(check))
print(f"part_sum : {part_sum}")
range_arr = []
for i in range(m):
    a, b = map(int, input().split())
    range_arr.append([a, b])
print(f"range_arr : {range_arr}")
for ra in range_arr:
    start = ra[0]
    end = ra[1]
    print(end - start + 1 - (part_sum[end] - part_sum[start - 1]))  # 전체 - (start 부터 end 까지 출석한 애들
