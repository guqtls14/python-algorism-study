"""
 *packageName    : 
 * fileName       : 2. 더맵게
 * author         : ipeac
 * date           : 2022-10-10
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-10        ipeac       최초 생성
 """
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    # 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야하는 최소 횟수 return
    while scoville[0] < K:
        
        min_scovile = heapq.heappop(scoville)
        two_scovile = heapq.heappop(scoville)
        mix = min_scovile + (two_scovile * 2)
        heapq.heappush(scoville, mix)
        answer += 1
        if len(scoville) <= 1 and scoville[0] < K:
            return -1
    return answer

# print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([0, 0, 1], 2))
