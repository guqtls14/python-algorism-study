"""
 *packageName    : 
 * fileName       : 2번
 * author         : jihye94
 * date           : 2022-08-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-06        jihye94       최초 생성
 """
import fractions


def solution(levels):
    print("levels : %s " % levels)
    
    if len(levels) < 4:
        return -1
    max_25 = len(levels) // fractions.Fraction(4, 3)
    print("max_25 : %s " % max_25)
    
    if len(levels[int(max_25):]) == 0:
        return -1
    
    while len(levels[int(max_25):]) > len(levels) / fractions.Fraction(4, 1):
        max_25 += 1
    print(levels[int(max_25):])
    print(levels[int(max_25):][0])
    return levels[int(max_25):][0]


solution([1])
print("==========================================")
solution([1, 2, 3, 4])
print("==========================================")
solution([1, 2, 3, 4, 5, 6, 7, 8, 9])
