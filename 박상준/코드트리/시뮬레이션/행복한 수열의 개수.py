"""
 *packageName    : 
 * fileName       : 행복한 수열의 개수
 * author         : ipeac
 * date           : 2022-10-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-18        ipeac       최초 생성
 """

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

answer = 0
seq = [0 for _ in range(n)]

def is_happy():
    # 주어진 seq 가 행복한 수열인지 판단
    consecutive_count, max_cnt = 1, 1
    for i in range(1, n):
        if seq[i - 1] == seq[i]:
            consecutive_count += 1
        else:
            consecutive_count = 1
        
        max_cnt = max(max_cnt, consecutive_count)
    
    return max_cnt >= m

# 가로 수행
for i in range(n):
    seq = graph[i][:]  # 주의!!!! 얇은 복사가 이루어 집니다,[:] 로 해당 깊은 복사를 해야합니다.
    
    if is_happy():
        answer += 1

#  세로 수행
for j in range(n):
    for i in range(n):
        seq[i] = graph[i][j]
    if is_happy():
        answer += 1

print(answer)
