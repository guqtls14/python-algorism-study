"""
 *packageName    : 
 * fileName       : 1182.부분 수열의 합
 * author         : ipeac
 * date           : 2022-10-02
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-02        ipeac       최초 생성
 """
n, s = map(int, input().split())
arr = list(map(int, input().split()))
# n, s = 2, -2
# arr = [-1, -1]
#
arr.sort()
a = []
cnt = 0

def dfs(start):
    global cnt
    if len(a) >= n:  # n 개수에 해당하며
        if sum(a) == s:  # 합이 s 인경우
            cnt += 1
        return
    
    else:
        if sum(a) == s and a:  # a가 존재한다면
            cnt += 1
        for i in range(start, n):
            a.append(arr[i])
            dfs(i + 1)
            a.pop()

dfs(0)
print(cnt)
