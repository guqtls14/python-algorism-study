"""
 *packageName    : 
 * fileName       : 1764.듣보잡
 * author         : ipeac
 * date           : 2022-09-09
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-09        ipeac       최초 생성
 """

# 듣도 못한 사람 n, 보도 못한 사람 m
n, m = map(int, input().split())

# n개줄 걸쳐 듣도 못한 사람 이름
no_listen = [input() for _ in range(n)]

# n+2 줄부터 보도 못한 사람의 이름
no_see = [input() for _ in range(m)]

# set
no_listen = set(no_listen)
no_see = set(no_see)

# 교집합
intersections = sorted(list(no_listen.intersection(no_see)))
print(len(intersections))
for i in intersections:
    print(i)
