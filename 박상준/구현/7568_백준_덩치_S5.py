"""
 *packageName    : 
 * fileName       : 7568_백준_덩치_S5
 * author         : jihye94
 * date           : 2022-07-25
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-25        jihye94       최초 생성
 """
# 전체 사람의 수
n = int(input())

n_arr = list(list(map(int, input().split())) for _ in range(n))

for value in n_arr:
    ranking = 1
    for value2 in n_arr:
        if value[0] < value2[0] and value[1] < value2[1]:
            ranking += 1
    print(ranking)
