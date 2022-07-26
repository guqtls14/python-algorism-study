"""
 *packageName    : 
 * fileName       : 1244_백준_스위치 켜고 끄기_S3
 * author         : ipeac
 * date           : 2022-07-26
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-26        ipeac       최초 생성
 """
#  n 스위치의 개수 ; 100이하인 양수

n = int(input())
# 각 스위치의 상태 1 켜져 0 꺼져
n_arr = list(map(int, input().split()))
# 학생의 수
stu_num = int(input())
# 학생의 성별,  학생이 받은 수 남 : 1 여 2 ; 스위치 개수 이하인 양수
stu_arr = [list(map(int, input().split())) for _ in range(stu_num)]

for line in stu_arr:
    if line[0] == 1:
        for i in range(line[1], len(n_arr) + 1, line[1]):
            n_arr[i - 1] = 1 if n_arr[i - 1] == 0 else 0

    elif line[0] == 2:
        n_arr[line[1] - 1] = 1 if n_arr[line[1] - 1] == 0 else 0

        minus = 2
        plus = 0
        while True:
            try:
                if line[1] - minus >= 0:
                    if n_arr[line[1] - minus] == n_arr[line[1] + plus]:
                        n_arr[line[1] - minus] = 1 if n_arr[line[1] - minus] == 0 else 0
                        n_arr[line[1] + plus] = 1 if n_arr[line[1] + plus] == 0 else 0
                        minus += 1
                        plus += 1
                    else:
                        break
                else:
                    break
            except IndexError:
                break
for index, value, in enumerate(n_arr):
    if index != 0 and index % 20 == 0:
        print()
    print(value, end=" ")
