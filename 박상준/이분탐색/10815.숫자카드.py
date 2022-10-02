"""
 *packageName    : 
 * fileName       : 10815.숫자카드
 * author         : ipeac
 * date           : 2022-09-26
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-26        ipeac       최초 생성
 """
# 상근이가 가진 카드의 개수 n
n = int(input())
# 상근이가 가진 카드 목록
cards = list(map(int, input().split()))
# 상근이가 가진 카드 검증 개수
m = int(input())
valid_cards = list(map(int, input().split()))

card_length = len(cards)

cards.sort()
for value in valid_cards:
    flag = False
    left = 0
    right = card_length - 1
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] == value:
            print(1, end=" ")
            flag = True
            break
        elif cards[mid] > value:
            right = mid - 1
        else:
            left = mid + 1
    if not flag:
        print(0, end=" ")
