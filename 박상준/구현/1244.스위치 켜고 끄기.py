"""
 *packageName    : 
 * fileName       : 1244.스위치 켜고 끄기
 * author         : qkrtkdwns3410
 * date           : 2022-09-09
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-09        qkrtkdwns3410       최초 생성
 """
# n 스위치의 개수
n = int(input())
# # 각 스위치의 상태
n_arr = list(map(int, input().split()))
print(f"n_arr : {n_arr}")
switch_status = []
for i, v in enumerate(n_arr):
    switch_status.append([i + 1, v])
print(f"switch_status : {switch_status}")

# # s_num 학생 수
s_num = int(input())
s_list = []

for i in range(s_num):
    sex, input_switch = map(int, input().split())
    s_list.append([sex, input_switch])

def same_check(left, right):
    print(f"left : {left}")
    print(f"right : {right}")
    if switch_status[left] == switch_status[right]:
        
        if left == right:
            switch_status[left] = 0 if switch_status[left] == 1 else 1
        else:
            switch_status[left] = 0 if switch_status[left] == 1 else 1
            switch_status[right] = 0 if switch_status[right] == 1 else 1
        
        if 0 < left and right < len(switch_status) - 1:
            left -= 1
            right += 1
            same_check(left, right)
        
        else:
            return left, right
    
    return left, right

for value in s_list:
    sex, input_swtich = value[0], value[1]
    if sex == 1:  # 남자
        for line in switch_status:
            if line[0] % input_swtich == 0:
                switch_status[line[0] - 1][1] = 1 if switch_status[line[0] - 1][1] == 0 else 0
    
    else:  # 여자
        left, right = same_check(input_swtich - 1, input_swtich - 1)
        print(f"switch_status : {switch_status}")

cnt = 0
for i in switch_status:
    print(i, end=" ")
    cnt += 1
    if cnt == 20:
        cnt = 0
        print()
