"""
 *packageName    : 
 * fileName       : 주차 요금 계산
 * author         : qkrtkdwns3410
 * date           : 2022-08-27
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-27        qkrtkdwns3410       최초 생성
 """

# fee 기본 시간(분) | 기본요금(원) | 단위 시간(분) | 단위 요금 (원)
import math
from collections import defaultdict


def solution(fees, records):
    answer = []
    default_time, default_charge, per_time, per_charge = map(int, fees)
    dic = defaultdict(list)
    for i, info in enumerate(records):
        time, car_num, infomation, = map(str, info.split(" "))
        dic[car_num].append(time)
    dic = sorted(dic.items())
    
    print(f"dic : {dic}")
    for line in dic:
        total_time = 0
        if len(line[1]) % 2 != 0:
            line[1].append('23:59')
            pass
        print(f"line[1] : {line[1]}")
        for i, each_time in enumerate(line[1]):
            if i % 2 == 0:
                time, minute = each_time.split(":")
                time_next, minute_next = line[1][i + 1].split(":")
                total_time += (int(time_next) * 60 + int(minute_next)) - (int(time) * 60 + int(minute))
                print(f"total_time : {total_time}")
        charge = 0
        
        if total_time > default_time:
            charge = default_charge + math.ceil((total_time - default_time) / per_time) * per_charge
            print(f"charge : {charge}")
        else:
            charge = default_charge
        
        answer.append(charge)
    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
