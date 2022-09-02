"""
 *packageName    : 
 * fileName       : 예상 대진표
 * author         : qkrtkdwns3410
 * date           : 2022-09-02
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-02        qkrtkdwns3410       최초 생성
 """

#  n 명 참가 , 토너먼트 형식
# n명 참가자 1~N 배정  12  3 4 56 ...n-1 n
# 다음 라운드 1~N//2 배정 >
# 1 2 다이다이 2 win > 다음 라운드 1번으로 배정
# 최종 한명이 남을 때까지 진행
# A 의 경쟁자 B 를 언제 만나는가?
# 서로 만나기 전까지 무조건 이긴다고 가정
def solution(n, a, b):
    answer = 0
    while True:
        if a == b:
            return answer
        a = (a + 1) // 2
        b = (b + 1) // 2
        answer += 1

print(solution(8, 4, 7))
