"""
 *packageName    : 
 * fileName       : 11652_백준_카드_S4
 * author         : jihye94
 * date           : 2022-07-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-23        jihye94       최초 생성
 """
import collections
import sys

input = sys.stdin.readline

most_common_one = sorted(collections.Counter(list(int(input()) for _ in range(int(input())))).items(),
                         key=lambda x: (-x[1], x[0]))
print(most_common_one.pop(0)[0])
