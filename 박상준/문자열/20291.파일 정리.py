"""
 *packageName    : 
 * fileName       : 20291.파일 정리
 * author         : qkrtkdwns3410
 * date           : 2022-09-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-06        qkrtkdwns3410       최초 생성
 """
from collections import defaultdict

import sys

input = sys.stdin.readline()
# 파일의 개수
n = int(input())
n_arr = []
for i in range(n):
    n_arr.append(input())

def solution(n, n_arr):
    dic = defaultdict(int)
    for i in range(n):
        n_s, n_e = map(str, n_arr[i].split("."))
        dic[n_e] += 1
    dic = sorted(dic.items())
    for value in dic:
        print(value[0], value[1])

solution(n, n_arr)
