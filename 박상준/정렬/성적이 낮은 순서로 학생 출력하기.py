"""
 *packageName    : 
 * fileName       : 성적이 낮은 순서로 학생 출력하기
 * author         : jihye94
 * date           : 2022-07-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-19        jihye94       최초 생성
 """
# 학생의 수 n
import sys

input = sys.stdin.readline

n = int(input())

n_arr = []

for i in range(n):
    name, score = map(str, input().split())
    n_arr.append([name, score])
n_arr.sort(key=lambda x: x[1])
for value in n_arr:
    print(value[0], end=" ")
