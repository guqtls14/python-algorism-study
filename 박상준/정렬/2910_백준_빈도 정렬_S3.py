"""
 *packageName    : 
 * fileName       : 2910_빈도 정렬_S3
 * author         : jihye94
 * date           : 2022-07-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-23        jihye94       최초 생성
 """
# 메시지의 길이
import collections

n, c = map(int, input().split())

m_arr = list(list(map(int, input().split())))
m_count = collections.Counter(m_arr).most_common()

for value in m_count:
    for i in range(value[1]):
        print(value[0], end=" ")
