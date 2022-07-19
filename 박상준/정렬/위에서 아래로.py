"""
 *packageName    : 
 * fileName       : 위에서 아래로
 * author         : jihye94
 * date           : 2022-07-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-19        jihye94       최초 생성
 """
import sys

input = sys.stdin.readline
# 수의 개수 n
n = int(input())
n_arr = []
for i in range(n):
    n_arr.append(int(input()))

n_arr.sort(reverse=True)
for value in n_arr:
    print(value, end=" ")
