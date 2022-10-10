"""
 *packageName    : 
 * fileName       : 다리를 지나는 트럭
 * author         : ipeac
 * date           : 2022-10-10
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-10        ipeac       최초 생성
 """
from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 다리에는 트럭이 최대 bridge_length 개 까지 버팁니다.
    # 다리는 weight 이하까지의 무게를 견딜 수 있습니다.
    # 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.
    answer = 0
    truck_weights = deque(truck_weights)
    going = deque([0] * bridge_length)
    
    bridge_weight = 0
    
    while going:
        answer += 1
        bridge_weight -= going.popleft()
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                going.append(truck)
                bridge_weight += truck
            else:
                going.append(0)
    print(answer)

print(solution(2, 10, [7, 4, 5, 6]))
# print(solution(100, 100, [10]))
# print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
