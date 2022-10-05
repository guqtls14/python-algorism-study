"""
 *packageName    : 
 * fileName       : 21921.블로그(2)
 * author         : ipeac
 * date           : 2022-10-05
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-05        ipeac       최초 생성
 """
# 블로그를 시작하고 지난 일수N 와 ~일 동안 가장 많이 돌어온 방문자 수와 그 기간
# x, n = 5, 2
x, n = map(int, input().split())
# blog = [1, 4, 2, 5, 1]
blog = list(map(int, input().split()))

length_blog = len(blog)  # 블로그 길이

if max(blog) == 0:  # 최대 방문자 수가 0 명 이라면 SAD
    print("SAD")
    exit()

start_pointer = 0
cnt = 1
sum_if = sum(blog[:n])
max_value = sum_if

for i in range(n, x):
    # 슬라이딩 윈도우 진행
    sum_if += blog[i]
    # 슬라이딩 윈도우 뒤의 값 제거
    sum_if -= blog[i - n]
    if sum_if > max_value:  # sum_if 가 max값보다 크다.
        max_value = sum_if
        cnt = 1
    elif sum_if == max_value:
        cnt += 1

print(max_value)
print(cnt)
