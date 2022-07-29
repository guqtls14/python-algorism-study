"""
 *packageName    : 
 * fileName       : 2161_카드1_S5
 * author         : jihye94
 * date           : 2022-07-29
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-29        jihye94       최초 생성
 """
from collections import deque

n_arr = deque()
for i in range(1, int(input()) + 1):
    n_arr.append(i)
answer = []
if len(n_arr) == 1:
    print(*n_arr)
while len(n_arr) >= 2:
    answer.append(n_arr.popleft())
    if len(n_arr) == 1:
        answer.append(n_arr.popleft())
        break
    n_arr.append(n_arr.popleft())

print(*answer)
