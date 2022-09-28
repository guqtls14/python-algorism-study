"""
 *packageName    : 
 * fileName       : 1756.피자굽기
 * author         : ipeac
 * date           : 2022-09-28
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-28        ipeac       최초 생성
 """
# 오븐의 깊이 D  ,반죽의 개수N
D, N = map(int, input().split())

# 오븐의 최상단부터 시작하여 깊이에 따른 오븐의 지름이 차례대로
oven_widths = list(map(int, input().split()))

# 피자반죽이 완성되는 순서대로 , 각각의 지름
pizza_widths = list(map(int, input().split()))

# 오븐의 최상단 1 , 최하단 가장 깊은 곳 D
# 만약 피자가 모두 오븐에 들어가지 않으면 0출력
for i in range(1, len(oven_widths)):
    oven_widths[i] = min(oven_widths[i], oven_widths[i - 1])

depth = D - 1
pizza_index = 0

for i in reversed(range(D)):
    if pizza_index >= len(pizza_widths):
        print(f"i : {i}")
        print(depth + 1)
        exit()
    
    if oven_widths[i] >= pizza_widths[pizza_index]:
        pizza_index += 1
        depth = i
print(0)
