"""
 *packageName    : 
 * fileName       : [3차]n진수 게임
 * author         : qkrtkdwns3410
 * date           : 2022-08-27
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-27        qkrtkdwns3410       최초 생성
 """


# 진법 n || 미리 구할 숫자의 갯수 t || 게임에 참가하는 인원 m || 튜브의 순서 p ||
# 2                                   4                             2                                   1
#
# n  10진법 숫자 || base 진법 변환
def convert(n, base):
    arr = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return arr[r]
    else:
        return convert(q, base) + arr[r]


def solution(n, t, m, p):
    answer = ''
    test = ''
    for i in range(m * t):
        test += (convert(i, n))
    print(f"test : {test}")
    while len(answer) < t:
        answer += test[p - 1]
        p += m
    return answer


print(solution(2, 4, 2, 1))  # "0111"
print(solution(16, 16, 2, 1))  # "02468ACE11111111"
print(solution(16, 16, 2, 2))  # "13579BDF01234567"
