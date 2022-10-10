"""
 *packageName    : 
 * fileName       : 20922.겹치는건 싫어!(2)
 * author         : ipeac
 * date           : 2022-10-05
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-05        ipeac       최초 생성
 """
# length, k = 9, 2
length, k = map(int, input().split())
# a = [3, 2, 5, 5, 6, 4, 4, 5, 7]
a = list(map(int, input().split()))

# 최장 연속 부분 수열의 길이 출력

start, end = 0, 0

max_length = 0
counter = [0] * (max(a) + 1)

while end < length:
    if counter[a[end]] < k:
        counter[a[end]] += 1
        end += 1
    else:
        counter[a[start]] -= 1
        start += 1
    max_length = max(max_length, end - start)
print(max_length)
