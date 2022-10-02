"""
 *packageName    : 
 * fileName       : 2661.좋은 수열(2)
 * author         : ipeac
 * date           : 2022-09-29
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-29        ipeac       최초 생성
 """
n = int(input())
# 숫자 1,2,3 으로만 이루어지는 수열
answer = ''

# 재귀를 위한 함수
def recursive(num):
    global n
    if len(num) == n:
        print(num)
        exit(0)
    for i in '123':
        if check(num + str(i)):
            recursive(num + str(i))
    return

# 좋은 수열인지 체크하는 함수
def check(num):
    # answer의 길이
    length = len(num)
    
    for idx in range(1, length // 2 + 1):
        if num[-idx:] == num[-(idx * 2): -idx]:
            return False
    else:
        return True

recursive('1')
