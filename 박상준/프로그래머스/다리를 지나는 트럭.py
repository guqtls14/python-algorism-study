"""
 *packageName    : 
 * fileName       : 다리를 지나는 트럭
 * author         : qkrtkdwns3410
 * date           : 2022-09-03
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-03        qkrtkdwns3410       최초 생성
 """

# 트럭은 최대 bridge_length대 만큼 올라갈 수 있으며
# 다리는 weight 이하의 무게까지 버틸수있고
# truck_weight : 트럭들의 무게
# 최단 시간안에 다리를 건너려면 .?
# 경과시간 || 다리를 지난 트럭 ||  건너는 트럭 || 대기트럭
from collections import deque

def solution(bridge_length, weight, truck_weights):
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
    
    return answer

# print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
# print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
