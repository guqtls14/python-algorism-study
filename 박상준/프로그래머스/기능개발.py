"""
 *packageName    : 
 * fileName       : 기능개발
 * author         : ipeac
 * date           : 2022-08-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-23        ipeac       최초 생성
 """


def solution(progresses, speeds):
    answer = []
    print(f"progresses : {progresses}")
    print(f"speeds : {speeds}")
    
    day_arr = []
    for i, value in enumerate(progresses):
        day_arr.append((100 - progresses[i]) // speeds[i] + 1 if (100 - progresses[i]) % speeds[i] != 0 else (100 - progresses[i]) // speeds[i])
    print(f"day_arr : {day_arr}")
    cnt = 1
    for i in range(1, len(day_arr)):
        if day_arr[i - 1] >= day_arr[i]:
            cnt += 1
            day_arr[i] = day_arr[i - 1]
        else:
            answer.append(cnt)
            cnt = 1
        if i == len(day_arr) - 1:
            answer.append(cnt)
    
    return answer


solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
print("==========================================")
solution([93, 30, 55], [1, 30, 5])
