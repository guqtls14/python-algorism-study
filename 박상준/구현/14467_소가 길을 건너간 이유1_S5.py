"""
 *packageName    : 
 * fileName       : 14467_소가 길을 건너간 이유1_S5
 * author         : ipeac
 * date           : 2022-08-17
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-17        ipeac       최초 생성
 """

n = int(input())
n_arr = [list(map(int, input().split())) for _ in range(n)]


# 소의 번호
# 길의 왼쪽 0 오른쪽 1
def solution(n, n_arr):
    cow_dict = dict()
    result = 0
    for line in n_arr:
        a, b = map(int, line)
        if a not in cow_dict:
            cow_dict[a] = b
        else:
            if cow_dict[a] != b:
                result += 1
                cow_dict[a] = b
    print(result)


solution(n, n_arr)
