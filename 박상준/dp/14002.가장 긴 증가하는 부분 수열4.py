"""
 *packageName    : 
 * fileName       : 14002.가장 긴 증가하는 부분 수열4
 * author         : ipeac
 * date           : 2022-09-26
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-26        ipeac       최초 생성
 """
# A 수열의 크기 N
n = int(input())
# 수열 A 를 이루고 있는 A_i
a = list(map(int, input().split()))
d = [0] * n

for i in range(n):
    d[i] = 1
    for j in range(0, i + 1):
        # A의 값이 이전의 값보다 큰지 검증 && dp 어레이의 이전값에서 +1 한
        # (즉, 길이가 더 긴 수열이라는 의미임.)
        # 결국 더 긴 수열인 경우 d에 기록해야함
        if a[i] > a[j] and d[i] < d[j] + 1:
            d[i] = d[j] + 1
print(max(d))

order = max(d)
answer = []
for i in range(n - 1, -1, -1):
    if d[i] == order:
        answer.append(a[i])
        order -= 1
answer.reverse()
print(*answer)
