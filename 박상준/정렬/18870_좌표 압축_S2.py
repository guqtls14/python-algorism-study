"""
 *packageName    : 
 * fileName       : 18870_좌표 압축_S2
 * author         : jihye94
 * date           : 2022-07-21
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-21        jihye94       최초 생성
 """
import sys

input = sys.stdin.readline

n = int(input())
n_arr = list(map(int, input().split()))

print("n_arr : %s " % n_arr)
n_arr_sorted = sorted(set(n_arr))
print("n_arr_sorted : %s " % n_arr_sorted)
dict = {n_arr_sorted[i]: i for i in range(len(n_arr_sorted))}
print("dict : %s " % dict)
for i in n_arr:
    print(dict[i], end=' ')
