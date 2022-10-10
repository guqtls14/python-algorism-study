"""
 *packageName    : 
 * fileName       : 1713.후보 추천하기
 * author         : ipeac
 * date           : 2022-10-10
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-10        ipeac       최초 생성
 """
from collections import defaultdict

n = int(input())
# n = 3
recom = int(input())
# recom = 9
recom_list = list(map(int, input().split()))
# recom_list = [2, 1, 4, 3, 5, 6, 2, 7, 2]
dic = defaultdict(lambda: 0)

for re_num in recom_list:
    if len(dic) == n and re_num not in dic.keys():
        key = list(dic.keys())
        value = list(dic.values())
        temp = value.index(min(value))
        idx = key[temp]
        del dic[idx]
    dic[re_num] += 1

print(*sorted(dic.keys()))
