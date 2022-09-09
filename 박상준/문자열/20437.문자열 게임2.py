"""
 *packageName    : 
 * fileName       : 20437.문자열 게임2
 * author         : qkrtkdwns3410
 * date           : 2022-09-08
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-08        qkrtkdwns3410       최초 생성
 """
# 문자열 게임의 수 T
from collections import defaultdict

t = int(input())

# 어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이를 구한다
# 어떤 문자를 정확히 K개를 포함하고, 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이를 구한다.
t_arr = []
for i in range(t):
    w = input()
    k = int(input())
    t_arr.append([w, k])

# t 수의 게임을 플레이한다,
for i in range(t):
    maax = 0
    miin = 10001
    
    dic = defaultdict(list)
    
    len_str = len(t_arr[i][0])
    value = t_arr[i][0]
    k = t_arr[i][1]
    
    # k 개 이상의 문자만 갈라냄
    for i in range(len_str):
        if value.count(value[i]) >= k:
            dic[value[i]].append(i)
    
    if not dic:
        print(-1)
        continue
    
    # 문자열의 첫번째와 마지막에 같은 가장 긴 연속 문자열 길이를 구해야함
    for idx in dic.values():
        for j in range(len(idx) - k + 1):
            len_tmp = idx[j + k - 1] - idx[j] + 1
            
            miin = len_tmp if len_tmp < miin else miin
            maax = len_tmp if len_tmp > maax else maax
    print(miin, maax)
