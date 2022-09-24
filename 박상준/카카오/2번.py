"""
 *packageName    : 
 * fileName       : 2번
 * author         : ipeac
 * date           : 2022-09-24
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-24        ipeac       최초 생성
 """

# n 개의 집 배달 | 배달다니면서 빈 재활용 상자 수거 | i 번째 집은 물류창고에서 i 만큼 떨어져있음. |
# 트럭에는 재활용 택배 상자를 최대 cap개 실을 수 있습니다
# 각 집마다 배달할 재활용 택배 상자의 개수 +               수거할 빈 재활용 택배 상자의 개수를 알고 있을 때,
# 트럭 하나로 모든 배달과 수거를 마치고                       물류창고까지 돌아올 수 있는              최소 이동 거리             를 구하려 합니다.
def solution(cap, n, deliveries, pickups):
    answer = 0
    
    # 해당 배열들의 원소가 전부 0인 경우에만
    while True:
        print("==========================================")
        print("초기")
        print(f"deliveries : {deliveries}")
        print(f"pickups    : {pickups}")
        # 용량 카운트
        my_cap = 0
        # 가야할 거리
        my_way = 0
        
        delivery_index = True
        
        # 최대 배달가능한 횟수
        delivery_load_balancing = cap
        
        # 배열을 반대로 돌기 시작한다.
        for i in range(n - 1, -1, -1):
            print(f"i : {i}")
            
            if delivery_index and (deliveries[i] != 0 or pickups[i] != 0):
                my_way = i + 1
                delivery_index = False
            
            if delivery_load_balancing >= deliveries[i] and deliveries[i] != 0:
                print(f"delivery_load_balancing : {delivery_load_balancing}")
                # 첫번째 배달인지 확인하기 위하여
                
                my_cap += deliveries[i]
                delivery_load_balancing -= deliveries[i]
                my_cap -= deliveries[i]
                deliveries[i] = 0
                print(f"delivery_load_balancing : {delivery_load_balancing}")
                print(f"deliveries : {deliveries}")
            if cap >= my_cap + pickups[i] and pickups[i] != 0:
                print("왓음?")
                my_cap += pickups[i]
                pickups[i] = 0
        # 제일 뒤의 배달장소의 길이를 담아준다.
        answer += my_way
        print("후기")
        print(f"deliveries : {deliveries}")
        print(f"pickups    : {pickups}")
        print("==========================================")
        if delivery_index:
            break
    # 배달 물건 설정 완료
    
    return answer * 2

# print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))  # 16
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))  # 30
