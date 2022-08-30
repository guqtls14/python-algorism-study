"""
 *packageName    : 
 * fileName       : 프린터
 * author         : ipeac
 * date           : 2022-08-31
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-31        ipeac       최초 생성
 """

def solution(priorities, location):
    answer = 0
    num = [(i, value) for i, value in enumerate(priorities)]
    print(f"num : {num}")
    while True:
        cur = num.pop(0)
        if any(cur[1] < q[1] for q in num):
            num.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
