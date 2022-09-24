"""
 *packageName    : 
 * fileName       : 3번
 * author         : ipeac
 * date           : 2022-09-24
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-24        ipeac       최초 생성
 """
from itertools import product

# 이모티콘 플러스 서비스 가입 수  || 이모티콘 매출액 ||  1차원 배열로 반환
def solution(users, emoticons):
    answer = []
    
    max_service_cnt = 0
    max_total_value = 0
    
    for combi in product([10, 20, 30, 40], repeat=len(emoticons)):  # 해당 할인율의 경우 회원들의 이모티콘 가입수 | 매출액 각각 최고점과 비교
        print(f"combi : {combi}")
        total_value = 0
        emoti_service_cnt = 0
        
        for user in users:
            dr, e_over = user[0], user[1]
            
            user_value = 0
            
            for i in range(len(combi)):  # 할인율 조합
                if combi[i] >= dr:  # 사용자의 할인율 기준이상인지 확인  || 만약 할인율 기준 미만이라면 구매자체를 안함
                    user_value += emoticons[i] * ((100 - combi[i]) / 100)  # 기준 이상이라면 값을 올린다.
            
            if int(user_value) >= e_over:  # 계산된 값이 서비스 가입 기준보다 높아면 바로 이모티콘 서비스에 가입할거임
                emoti_service_cnt += 1
            else:
                total_value += int(user_value)
            # 넘지않았으니 total
        if max_service_cnt < emoti_service_cnt:  # 서비스 가입자 수가 최대인 경우 무조건 다 담아준다.
            max_service_cnt = emoti_service_cnt
            max_total_value = total_value
        elif max_service_cnt == emoti_service_cnt and max_total_value < total_value:  # 서비스 가입자 수가 동일한데 매출액이 더 큰 경우 해당 매출액을 비교후 판별
            max_total_value = total_value
        # 나머지는 판별할 가치없음
    
    answer.append(max_service_cnt)
    answer.append(max_total_value)
    
    return answer

# print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
print(solution(
    [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))
