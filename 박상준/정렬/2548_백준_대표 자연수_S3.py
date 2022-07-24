"""
 *packageName    : 
 * fileName       : 2548_백준_대표 자연수_S3
 * author         : jihye94
 * date           : 2022-07-24
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-24        jihye94       최초 생성
 """
n = int(input())
n_arr = list(map(int, input().rstrip().split()))
n_arr.sort()
result = []
if len(n_arr) % 2 == 0:
    print(n_arr[len(n_arr) // 2 - 1])
else:
    print(n_arr[len(n_arr) // 2])
