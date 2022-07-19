"""
 *packageName    : 
 * fileName       : 두 배열의 원소 교체
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

# n = 배열의 길이 || k  = 바꿔치기 가능한 횟수
n, k = map(int, input().split())

a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]

print(sum(a))
