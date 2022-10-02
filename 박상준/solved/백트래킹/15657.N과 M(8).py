"""
 *packageName    : 
 * fileName       : 15657.N과 M(8)
 * author         : ipeac
 * date           : 2022-10-02
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-02        ipeac       최초 생성
 """
n, m = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

s = []

def dfs(start):
    if m == len(s):
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, n):
        s.append(arr[i])
        dfs(i)
        s.pop()

dfs(0)
