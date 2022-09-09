"""
 *packageName    : 
 * fileName       : 20436.ZOAC3
 * author         : qkrtkdwns3410
 * date           : 2022-09-08
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-08        qkrtkdwns3410       최초 생성
 """
"""
z o
zoac
"""

left = [['q', 'w', 'e', 'r', 't'],
        ['a', 's', 'd', 'f', 'g'],
        ['z', 'x', 'c', 'v']]
right = [['', '', '', '', '', 'y', 'u', 'i', 'o', 'p'],
         ['', '', '', '', '', 'h', 'j', 'k', 'l'],
         ['', '', '', '', 'b', 'n', 'm']]

# sl, sr = map(str, input().split(" "))
# alpha = input()
# 테스트용
sl, sr = 'z', 'o'
alpha = list('l')

# 왼손에 해당하는 값인지 체크 아닌 경우 -1 반환
def return_left_location(string):
    answer_return = -1
    for i in range(len(left)):
        for j in range(len(left[i])):
            if left[i][j] == string:
                answer_return = [i, j]
    return answer_return

# 오른손에 해당하는 값인지 체크 아닌 경우 -1 반환
def return_right_location(string):
    answer_return = -1
    for i in range(len(right)):
        for j in range(len(right[i])):
            if right[i][j] == string:
                answer_return = [i, j]
    
    return answer_return

# 왼손 값 세팅
sl = return_left_location(sl)
# 오른손 값 세팅
sr = return_right_location(sr)

answer = 0

for value in alpha:
    # 만약 해당 값이 오른손값이라면
    if return_left_location(value) == -1:
        # 값의 로케이션 반환
        value_location = return_right_location(value)
        # 해당 값의 택시거리 계산
        sr_cha = abs(sr[0] - value_location[0]) + abs(sr[1] - value_location[1])
        # 오른손 값 세팅
        sr = value_location
        # 택시거리 + 버튼 누르는 1 시간
        answer += sr_cha + 1
    
    
    elif return_right_location(value) == -1:
        value_location = return_left_location(value)
        sl_cha = abs(sl[0] - value_location[0]) + abs(sl[1] - value_location[1])
        sl = value_location
        answer += sl_cha + 1

print(answer)
