"""
 *packageName    : 
 * fileName       : 금 채굴하기[solution2]
 * author         : ipeac
 * date           : 2022-10-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-18        ipeac       최초 생성
 """
# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 주어진 k에 대하여 마름모의 넓이를 반환한다.
def get_area(k):
    return k * k + (k + 1) * (k + 1)

# 주어진 좌표가 격자에 포함되는지 여부를 반환한다.
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def get_num_of_gold(row, col, k):
    num_of_gold = 0
    # 방향에 따라 바뀌는 x와 y의 변화량을 정의한다.
    dxs=[1,1,-1,-1]
    dys=[-1,1,1,-1]
    
    num_of_gold+=grid[row][col]# k = 0 일 때 처리
    
    
    
