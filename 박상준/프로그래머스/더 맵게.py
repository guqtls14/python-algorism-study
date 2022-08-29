"""
 *packageName    : 
 * fileName       : 더 맵ㄱ
 * author         : ipeac
 * date           : 2022-08-29
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-29        ipeac       최초 생성
 """

# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        print(f"scoville : {scoville}")
        if scoville[0] >= K:
            break
        if len(scoville) <= 1:
            return -1
        answer += 1
        small = heapq.heappop(scoville)
        small2 = heapq.heappop(scoville)
        snum = small + (small2 * 2)
        
        heapq.heappush(scoville, snum)
    
    return answer

print(solution([1, 1], 7))
