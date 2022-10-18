"""
 *packageName    : 
 * fileName       : 14500.테트로미노
 * author         : ipeac
 * date           : 2022-10-17
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-17        ipeac       최초 생성
 """
import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

# n, m = map(int, input().split())
# print(f"n, m = {n, m}")
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input().split())))
# print(f"graph = {graph}")

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

n, m = (5, 5)
graph = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [2, 3, 4, 5, 6], [6, 5, 4, 3, 2], [1, 2, 1, 2, 1]]
visited = [[False] * m for _ in range(n)]

def dfs(i, j, depth, visited):
    visited[i][j] = True
    for i in range(4):
        nx = i + dx[i]
        ny = j + dy[i]
        
        if nx < 0 or nx > n or ny < 0 or ny > m:
            continue
        if not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, visited)
            visited[nx][ny] = False

for i in range(m):
    for j in range(n):
        dfs(i, j, 0, visited)
