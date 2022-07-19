"""
 *packageName    : 
 * fileName       : 10825_백준_국영수
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
# n 명
n = int(input())
n_arr = []
for i in range(n):
    name, korean, eng, math = map(str, input().split())
    n_arr.append([name, int(korean), int(eng), int(math)])
n_arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for arr in n_arr:
    print(arr[0])
