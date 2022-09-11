"""
 *packageName    : 
 * fileName       : 22864.피로도
 * author         : qkrtkdwns3410
 * date           : 2022-09-11
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-11        qkrtkdwns3410       최초 생성
 """
# 한시간 일하면 a 피로도 UP, b만큼 일처리 | 한시간 쉬면 c피로도 down
# m 피로도의 한계치
# 24시간동안 일 최대치
# a, b, c, m = map(int, input().split())
a, b, c, m = 11, 5, 1, 10
time = 0
piro = 0
answer = 0
while time <= 23:
    if piro <= m - a:
        # 일해야함
        answer += b
        piro += a
        pass
    elif piro > m - a:
        # 휴식필요
        piro -= c
        if piro < 0:
            piro = 0
    time += 1
print(answer)
