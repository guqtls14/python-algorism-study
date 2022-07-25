"""
 *packageName    : 
 * fileName       : 10773_제로_S4
 * author         : jihye94
 * date           : 2022-07-25
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-25        jihye94       최초 생성
 """

k = int(input())
answer = []
for i in range(k):
    input_value = int(input())
    if input_value == 0:
        answer.pop()

    else:
        answer.append(input_value)

print(sum(answer))
