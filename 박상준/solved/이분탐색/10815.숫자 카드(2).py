"""
 *packageName    : 
 * fileName       : 10815.숫자 카드(2)
 * author         : ipeac
 * date           : 2022-10-09
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-09        ipeac       최초 생성
 """

n = int(input())
card_sg = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))

card_sg.sort()

# 상근이가 가지고 있는 카드인지 아닌지 체크해야합니다.
for t_value in target:
    start = 0
    end = len(card_sg) - 1
    flag = False
    
    while start <= end:
        mid = (start + end) // 2
        
        if card_sg[mid] > t_value:
            end = mid - 1
        elif card_sg[mid] < t_value:
            start = mid + 1
        else:
            flag = True
            print(1, end=" ")
            break
    if not flag:
        print(0, end=" ")
