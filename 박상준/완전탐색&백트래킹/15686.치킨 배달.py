"""
 *packageName    : 
 * fileName       : 15686.치킨 배달
 * author         : ipeac
 * date           : 2022-09-30
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-30        ipeac       최초 생성
 """
from itertools import combinations

# 크기가 n*  n인 도시있음
# 빈칸 0 집 1 치킨집2
# 행 r 열 c 행열은 1부터 시작
# 치킨거리 : 집과 가장 가까운 치킨집 사이의 거리
# 도시의 치킨 거리 =  모든 집의 치킨거리의 합
# 임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|로 구한다
#
# 도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업
# 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을
n, m = map(int, input().split())
# city = [list(map(int, input().split())) for _ in range(n)]
city = [list(map(int, input().split())) for _ in range(n)]

min_chicken_dis = 10e9

chicken = []
home = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            # home
            home.append([i, j])
        elif city[i][j] == 2:
            # chicken
            chicken.append([i, j])

for chi in combinations(chicken, m):
    # 도시간의 치킨의 거리
    tmp = 0
    for ho in home:
        # 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리
        chi_len = 10e9  # 각 집마다의 치킨거리
        for j in range(m):
            chi_len = min(chi_len, abs(ho[0] - chi[j][0]) + abs(ho[1] - chi[j][1]))
        tmp += chi_len
    min_chicken_dis = min(min_chicken_dis, tmp)

print(min_chicken_dis)
