"""
 *packageName    : 
 * fileName       : 21921.블로그
 * author         : ipeac
 * date           : 2022-10-04
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-04        ipeac       최초 생성
 """
# 블로그를 시작하고 지난 일수 N 와 X (x일 동안 가장 많이 들어온 방문자수 기간 파악)
# N, X = map(int, input().split())
N, X = [5, 2]
# blog_arr = list(map(int, input().split()))  # 블로그 시작 1일차부터 N일차까지 하루 방문자 수가 공백으로 구분되어 주어진다.
blog_arr = [1, 4, 2, 5, 1]  # 블로그 시작 1일차부터 N일차까지 하루 방문자 수가 공백으로 구분되어 주어진다.
if max(blog_arr) == 0:
    print("SAD")
else:
    value = sum(blog_arr[:X])
    
    max_value = value
    max_cnt = 1
    
    for i in range(X, N):
        # 슬라이딩 윈도우 진행
        value += blog_arr[i]
        # 슬라이딩 윈도우 뒤의 값 제거
        value -= blog_arr[i - X]
        if value > max_value:
            max_value = value
            max_cnt = 1
        elif value == max_value:
            max_cnt += 1
    
    print(max_value)
    print(max_cnt)

"""
첫째 줄에 X일 동안 가장 많이 들어온 방문자 수를 출력한다.
만약 최대 방문자 수가 0명이라면 SAD를 출력한다.

만약 최대 방문자 수가 0명이 아닌 경우 둘째 줄에 기간이 몇 개 있는지 출력한다.
"""
