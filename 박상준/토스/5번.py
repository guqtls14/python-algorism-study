"""
 *packageName    : 
 * fileName       : 5번
 * author         : jihye94
 * date           : 2022-08-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-06        jihye94       최초 생성
 """
from collections import Counter


def solution(tasks):
    print("tasks : %s " % tasks)
    c = Counter(tasks)
    tasks__items = c.items()
    counter = list(tasks__items)
    print("counter : %s " % counter)
    
    for items in counter:
        print(items[1])
        if items[1] != 2 and items[1] != 3:
            return -1
    print("c.keys() : %s " % c.keys())
    return len(c.keys())


solution([1])
print("==========================================")
solution([1, 1, 2, 3, 3, 2, 2])
print("==========================================")
solution([4, 1, 1, 1, 1, 2, 3])
print("==========================================")
solution([1, 1, 2, 2])
