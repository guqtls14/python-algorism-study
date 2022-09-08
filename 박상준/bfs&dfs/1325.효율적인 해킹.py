"""
 *packageName    : 
 * fileName       : 1325.효율적인 해킹
 * author         : qkrtkdwns3410
 * date           : 2022-09-08
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-08        qkrtkdwns3410       최초 생성
 """
# n ; 컴퓨터 수 ; m;  신뢰 수
# 양방향
# n, m, = map(int, input().split(" "))
# node = [[] * (n + 1) for _ in range(n + 1)]
# for _ in range(m):
#     a, b = map(int, input().split(" "))
#     node[a].append(b)
#     node[b].append(a)
n, m = 5, 4
node = [[3, 1], [3, 2], [4, 3], [5, 3]]
