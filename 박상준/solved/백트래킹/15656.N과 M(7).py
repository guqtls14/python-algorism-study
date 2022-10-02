"""
 *packageName    : 
 * fileName       : 15656.N과 M(7)
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

s = []
arr.sort()

def dfs():
    if m == len(s):
        print(' '.join(map(str, s)))
        return
    for i in range(0, n):
        s.append(arr[i])
        dfs()
        s.pop()

dfs()
