"""
 *packageName    : 
 * fileName       : 1939.중량제한
 * author         : ipeac
 * date           : 2022-09-28
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-28        ipeac       최초 생성
 """
# n 개의 섬 m개의 줄 다리에 대한 정보
# n, m = map(int,input().split())
n, m = 3, 3
bridge = [[] for _ in range(n + 1)]

# a 와 b 섬사이에 중량제한이 c인 다리가 존재
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     bridge[a].append([b, c])
#     bridge[b].append([a, c])

bridge = [[], [[2, 2], [3, 3]], [[1, 2], [3, 2]], [[1, 3], [2, 2]]]

# 출발 도착
starter, destination = 1, 3

# 한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값 구하기
# 시발!
