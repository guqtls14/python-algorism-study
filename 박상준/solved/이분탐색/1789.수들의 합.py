"""
 *packageName    : 
 * fileName       : 1789.수들의 합
 * author         : ipeac
 * date           : 2022-10-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-06        ipeac       최초 생성
 """
s = int(input())
# 서로 다른 N개 자연수의 합 s
count = 1
sum = 0
while s >= sum:
    sum += count
    count += 1
print(count - 2)
