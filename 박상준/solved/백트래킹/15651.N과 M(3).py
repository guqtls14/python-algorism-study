"""
 *packageName    : 
 * fileName       : 15651.N과 M(3)
 * author         : ipeac
 * date           : 2022-10-01
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-01        ipeac       최초 생성
 """
n, m = 4, 2

s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n + 1):
        s.append(i)
        dfs()
        s.pop()

dfs()
