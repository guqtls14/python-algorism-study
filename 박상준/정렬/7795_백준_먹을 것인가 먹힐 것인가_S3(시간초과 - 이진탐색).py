"""
 *packageName    : 
 * fileName       : 7795_백준_먹을 것인가 먹힐 것인가_S3
 * author         : jihye94
 * date           : 2022-07-24
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-24        jihye94       최초 생성
 """
import bisect

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())

    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))

    result = 0
    for value in a:
        result += bisect.bisect(b, value - 1)
    print(result)
