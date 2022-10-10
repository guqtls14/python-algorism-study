"""
 *packageName    : 
 * fileName       : 11728.배열 합치기
 * author         : ipeac
 * date           : 2022-10-04
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-04        ipeac       최초 생성
 """
N, M = map(int, input().split())
# 배열 A 의 크기 N , 배열 B 의 크기 M
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# A = [3, 5]
# B = [2, 9]
a_pointer, b_pointer = 0, 0
a_length, b_length = len(A), len(B)

answer = []

while a_pointer != a_length or b_pointer != b_length:
    if a_pointer == a_length:
        answer.append(B[b_pointer])
        b_pointer += 1
    elif b_pointer == b_length:
        answer.append(A[a_pointer])
        a_pointer += 1
    else:
        if A[a_pointer] > B[b_pointer]:
            answer.append(B[b_pointer])
            b_pointer += 1
        else:
            answer.append(A[a_pointer])
            a_pointer += 1
print(*answer)
