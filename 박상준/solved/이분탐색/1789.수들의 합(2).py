"""
 *packageName    : 
 * fileName       : 1789.수들의 합(2)
 * author         : ipeac
 * date           : 2022-10-09
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-09        ipeac       최초 생성
 """
s = int(input())
count = 1
max_of = 0
while count * (count + 1) / 2 <= s:
    count += 1

print(count - 1)
