"""
 *packageName    : 
 * fileName       : 14888.연산자 끼워넣기
 * author         : ipeac
 * date           : 2022-09-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-18        ipeac       최초 생성
 """
# 수의 개수
import math

n = 6
arr = [1, 2, 3, 4, 5, 6]
_max = -1e9
_min = 1e9

# 합이 n-1 인 4개의 정수 || 덧셈 뺏셈 곱셈 나눗셈의 개수
calc_arr = [2, 1, 1, 1]
plus = calc_arr[0]
minus = calc_arr[1]
multi = calc_arr[2]
div = calc_arr[3]


def dfs(depth, total, plus, minus, multi, div):
    global _max
    global _min

    if depth == n:
        _max = max(total, _max)
        _min = min(total, _min)
        return
    if plus:
        dfs(depth + 1, total + arr[depth], plus - 1, minus, multi, div)
    if minus:
        dfs(depth + 1, total - arr[depth], plus, minus - 1, multi, div)
    if multi:
        dfs(depth + 1, total * arr[depth], plus, minus, multi - 1, div)
    if div:
        dfs(depth + 1, int(total / arr[depth]), plus, minus, multi, div - 1)


dfs(1, arr[0], plus, minus, multi, div)
print(_max)
print(_min)
