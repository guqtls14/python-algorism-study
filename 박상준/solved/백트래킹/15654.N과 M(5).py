"""
 *packageName    : 
 * fileName       : 15654.N과 M(5)
 * author         : ipeac
 * date           : 2022-10-02
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-02        ipeac       최초 생성
 """
n, m = map(int, input().split())
# N개의 자연수 중에서 M개를 고른 수열

arr = list(map(int, input().split()))
arr.sort()

s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(0, n):
        if arr[i] in s:
            continue
        
        s.append(arr[i])
        dfs()
        s.pop()

dfs()
