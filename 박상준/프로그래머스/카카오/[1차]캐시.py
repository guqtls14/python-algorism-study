"""
 *packageName    : 
 * fileName       : [1차]캐시
 * author         : ipeac
 * date           : 2022-08-24
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-24        ipeac       최초 생성
 """
from collections import deque


def solution(cacheSize, cities):
    cities = list(value.lower() for value in cities)
    print(f"cities : {cities}")
    cache = deque()
    print(f"cache : {cache}")
    time = 0
    for city in cities:
        if len(cache) < cacheSize:
            if city in cache:
                time += 1
                cache.append(city)
                cache.remove(city)
            elif city not in cache:
                cache.append(city)
                time += 5
        
        elif len(cache) >= cacheSize:
            if city in cache:
                time += 1
                cache.append(city)
                cache.remove(city)
            elif city not in cache:
                time += 5
                cache.append(city)
                cache.popleft()
    print(f"time : {time}")
    return time


# solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
# solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])
# solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
# solution(1, ["a", "a", "A"])
solution(3, ["A", "B", "A", "C"])
