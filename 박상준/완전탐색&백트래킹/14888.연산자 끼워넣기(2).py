"""
 *packageName    : 
 * fileName       : 14888.연산자 끼워넣기(2)
 * author         : ipeac
 * date           : 2022-09-30
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-30        ipeac       최초 생성
 """
n = int(input())
# 식
a = list(map(int, input().split()))

_max = -10e9
_min = 10e9

# 연산자 더하기 |  빼기 | 곱셈 | 나눗셈
calc = list(map(int, input().split()))
plus = calc[0]
minus = calc[1]
prod = calc[2]
divd = calc[3]

# 만들수있는 식의 최대 값, 최소 값 출력

def dfs(depth, total, plus, minus, prod, divd):
    global _max, _min
    
    if depth == n:
        _max = max(total, _max)
        _min = min(total, _min)
        return
    
    if plus:
        dfs(depth + 1, total + a[depth], plus - 1, minus, prod, divd)
    
    if minus:
        dfs(depth + 1, total - a[depth], plus, minus - 1, prod, divd)
    
    if prod:
        dfs(depth + 1, total * a[depth], plus, minus, prod - 1, divd)
    
    if divd:
        dfs(depth + 1, int(total / a[depth]), plus, minus, prod, divd - 1)

dfs(1, a[0], plus, minus, prod, divd)
print(_max)
print(_min)
