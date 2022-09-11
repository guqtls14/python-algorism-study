"""
 *packageName    : 
 * fileName       : 22858.원상 복구(small)
 * author         : qkrtkdwns3410
 * date           : 2022-09-11
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-11        qkrtkdwns3410       최초 생성
 """
# 1부터 n 까지 d1,d2,,,,dn
# D1 = 4 P4 의 값을 4번째로 가지고옴. 3
# D2 = 3 P2의 값을 2번째로 가지고옴. 4
# D
# 카드 개수 n : 카드를 섞은 횟수인 K가 공백
n, k = map(int, input().split())
S = list(map(int, input().split()))
D = list(map(int, input().split()))
# n, k = 5, 2
# S = [4, 1, 3, 5, 2]
# D = [4, 3, 1, 2, 5]
for j in range(k):
    tmp = [0] * n
    for j, value in enumerate(S):
        tmp[D[j] - 1] = value
    S = tmp
print(*S)
