"""
 *packageName    : 
 * fileName       : 15652.N과 M(4)
 * author         : ipeac
 * date           : 2022-10-02
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-02        ipeac       최초 생성
 """
n, m = 4, 2
# m개를 고른다.!
# 같은 수를 여러개

s = []

def dfs(start):
    if m == len(s):
        print(' '.join(map(str, s)))
        return
    for i in range(start, n + 1):
        s.append(i)
        dfs(i)
        s.pop()

dfs(1)
