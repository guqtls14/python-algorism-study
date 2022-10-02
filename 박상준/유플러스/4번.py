"""
 *packageName    : 
 * fileName       : 4번
 * author         : ipeac
 * date           : 2022-10-01
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-01        ipeac       최초 생성
 """
import math

answer = 0
tmp = 0

def dp(players):
    global tmp
    global answer
    if len(players) == 1:
        answer = answer if answer > tmp else tmp
        
        return tmp
    new_players = []
    for i in range(0, len(players), 2):
        left = players[i]
        right = players[i + 1]
        if left == 1 or right == 1:
            tmp += 1
            new_players.append(1)
        elif left == 0 and right == 0:
            new_players.append(0)
    dp(new_players)

def check(players):
    flag = False
    for i in range(0, len(players), 2):
        left = players[i]
        right = players[i + 1]
        if left == 0 and right == 0:
            flag = True
    
    if flag:
        return False  # 0 0 인 친구가 또 존재함;;
    else:
        
        return True

def sum_it(players):
    sum_ = 0
    length = len(players) // 2
    index = length // 2
    for i in range(length, 0, -index):
        index //= 2
        sum_ += i
    return sum_ + 1

def solution(players):
    global tmp
    chk = False
    for i in range(0, len(players), 2):
        left = players[i]
        right = players[i + 1]
        if left == 0 and right == 0:
            chk = True
            players[i] = 1
            if check(players):
                dp(players)
            
            else:
                return sum_it(players)
            players[i] = 0
    if not chk:
        return sum_it(players)
    
    return answer

print(solution([1, 0, 0, 1, 0, 0, 1, 0]))
# print(solution([0, 0, 0, 1]))
# print(solution([0, 1, 1, 0, 0, 1, 1, 0]))
# print(solution([1, 0, 1, 0, 1, 0, 1, 0]))
