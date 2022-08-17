"""
 *packageName    : 
 * fileName       : 체육복 도둑
 * author         : ipeac
 * date           : 2022-08-17
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-17        ipeac       최초 생성
 """


def solution(n, lost, reserve):
    answer = 0
    # 잃어버린 친구들 개수 뻄
    n -= len(lost)
    
    for index in range(len(reserve)):
        for index2 in range(len(lost)):
            if reserve[index] - 1 == lost[index2] or reserve[index] + 1 == lost[index2]:
                n += 1
                lost.pop(index2)
                break
    return n


solution(5, [2, 4], [1, 3, 5])
print("==========================================")
solution(5, [2, 4], [3])
print("==========================================")
solution(3, [3], [1])
print("==========================================")
