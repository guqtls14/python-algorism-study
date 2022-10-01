"""
 *packageName    : 
 * fileName       : 9663.N-QUEEN
 * author         : ipeac
 * date           : 2022-10-01
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-01        ipeac       최초 생성
 """
n = 8
ans = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    pass

def n_queen(x):
    global ans
    if x == n:
        ans += 1
        return
    
    else:
        for i in range(n):  # 만큼 반복한다. #행단위로 반복하기에 추후 행단위 체크는 불필요하다.
            if is_promising(x):  # 퀸의 유효성 체크 | 같은 열에 있는지 체크한다.
                # [x, i]에 퀸을 놓겠다.
                row[x] = i
                n_queen(x + 1)

n_queen(0)  # 0행부터 시작한다.
print(ans)
