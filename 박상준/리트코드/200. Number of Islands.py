"""
 *packageName    : 
 * fileName       : 200. Number of Islands
 * author         : ipeac
 * date           : 2022-10-11
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-11        ipeac       최초 생성
 """
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from collections import deque
from typing import *

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def Solution(grid: List[List[str]]) -> int:
    visited = [[0] * len(grid[0]) for _ in range(len(grid))]
    cnt = 0
    
    def bfs(i, j):
        q = deque()
        q.append([i, j])
        visited[i][j] = 1
        
        while q:
            x, y = q.popleft()
            for xx, yy in zip(dx, dy):
                nx = xx + x
                ny = yy + y
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not visited[nx][ny] and grid[nx][ny] == '1':
                    q.append([nx, ny])
                    visited[nx][ny] = 1
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not visited[i][j] and grid[i][j] == '1':
                bfs(i, j)
                cnt += 1
    return cnt

"""print(Solution(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))"""
print(Solution(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
