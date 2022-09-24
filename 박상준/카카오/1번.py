"""
 *packageName    : 
 * fileName       : 1번
 * author         : ipeac
 * date           : 2022-09-24
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-24        ipeac       최초 생성
 """
from collections import defaultdict

# 개인정보 n 개
def solution(today, terms, privacies):
    answer = []
    
    t_year, t_month, t_day = map(str, today.split("."))
    
    today = str(t_year) + str(t_month) + str(t_day)
    
    # 유효기간 dic으로 정리
    expire_dic = defaultdict(int)
    for line in terms:
        line = line.split(" ")
        expire_dic[line[0]] = line[1]
    
    # 날짜 약관날짜로 해석
    for i, line in enumerate(privacies):
        day, type = map(str, line.split())
        year, month, day = map(int, day.split('.'))
        print(f"line : {line}")
        month += int(expire_dic[type])
        year_over = 0
        
        # 초과되는 달 변환
        while month // 13 >= 1:
            month -= 12
            year_over += 1
        month = str(month)
        day = str(day)
        year += year_over
        
        if len(month) == 1:
            month = '0' + month
        if len(day) == 1:
            day = '0' + day
        
        day = str(year) + str(month) + str(day)
        print(f"day : {day}")
        print(f"today : {today}")
        
        # 현재일과 비교 후 초과 날짜 < 현재일 answer에  privacies 인덱스를 answer에 담습니다.
        if int(today) >= int(day):
            answer.append(i + 1)
    
    return answer

# print(solution("2020.05.19", ["A 6", "B 12", "C 3"], ["0000.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))  # [1,3]
print(solution("2021.12.02", ["A 0"], ["2021.12.02 A"]))  # [1,3]
# print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))  # [1,4,5]
