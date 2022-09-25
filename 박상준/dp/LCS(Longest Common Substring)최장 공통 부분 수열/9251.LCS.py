"""
 *packageName    : 
 * fileName       : 9251.LCS
 * author         : ipeac
 * date           : 2022-09-25
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-25        ipeac       최초 생성
 """
String_a = input()
String_b = input()

length_a = len(String_a)
length_b = len(String_b)
lcs = [[0] * (length_b + 1) for _ in range(length_a + 1)]  # 마진 grid 설정 세로값 b의 길이 || 가로 값 a의 길이

for i in range(1, length_a + 1):
    for j in range(1, length_b + 1):
        if String_a[i - 1] == String_b[j - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

print(lcs[-1][-1])
