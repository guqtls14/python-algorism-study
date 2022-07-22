"""
 *packageName    : 
 * fileName       : 1015_수열 정렬_S4
 * author         : ipeac
 * date           : 2022-07-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-23        ipeac       최초 생성
 """
import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = []
sorted_a = sorted(a)
for i in range(n):
    # 인덱스는 앞에서부터 검색됨
    index = sorted_a.index(a[i])
    b.append(index)
    # 고로 sorted된 배열의 값을 검색하지 못하도록 임의의 음수로 지정
    sorted_a[index] = -1
print(*b)
