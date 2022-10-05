"""
 *packageName    : 
 * fileName       : 15961.회전 초밥
 * author         : ipeac
 * date           : 2022-10-05
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-05        ipeac       최초 생성
 """
from collections import defaultdict

# 접시수 n ; 초밥의 가짓수 d ; 연속해서 먹는 접시의 수 k, 쿠폰 번호 c
n, d, k, c = 8, 30, 4, 30
sushi = [7, 9, 7, 30, 2, 7, 9, 25]
sushi.extend(sushi)

dic = defaultdict(int)

result = 0
# 초밥의 가짓수의 최댓값 하나의 정수로 출력
# 슬라이딩 윈도우...
left = 0
right = 0

dic[c] += 1  # 보너스는 무조건 먹는다.

# 1. 처음에 k 구간만큼 먹는다
while right < k:
    dic[sushi[right]] += 1
    right += 1

# 2. 슬라이딩 윈도우 적용
while right < n:
    result = max(result, len(dic))
    # 1. 맨 왼쪽의 초밥 제거
    dic[sushi[left]] -= 1
    if dic[sushi[left]] == 0:  # 삭제된 왼쪽 초밥이 0 인 경우 dict 삭제
        del dic[sushi[left]]
    # 2. 오른쪽 초밥 추가하기
    dic[sushi[right]] += 1
    # 왼쪽과 오른쪽 위치 +1
    left += 1
    right += 1
print(result)
