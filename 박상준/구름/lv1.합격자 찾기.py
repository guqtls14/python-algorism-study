"""
 *packageName    : 
 * fileName       : lv1.합격자 찾기
 * author         : ipeac
 * date           : 2022-10-10
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-10        ipeac       최초 생성
 """
t = int(input())
# 응시 인원수
for i in range(t):
    n = int(input())
    # 시험성적
    v = list(map(int, input().split()))
    avg = sum(v) / n
    count = 0
    for score in v:
        if score >= avg:
            count += 1
    print(f"{count}/{n}")
