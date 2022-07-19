"""
 *packageName    : 
 * fileName       : 18310_백준_안테나
 * author         : jihye94
 * date           : 2022-07-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-19        jihye94       최초 생성
 """
# 집의 수
n = int(input())
n_arr = list(map(int, input().split()))

print("n_arr : %s " % n_arr)
n_arr.sort()
print(n_arr[(n - 1) // 2])
