"""
 *packageName    : 
 * fileName       : 11728.배열 합치기(2)
 * author         : ipeac
 * date           : 2022-10-05
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-05        ipeac       최초 생성
 """
length_a, length_b = map(int, input().split())
# length_a, length_b = 2, 1
a = list(map(int, input().split()))
# a = [4, 7]
b = list(map(int, input().split()))
# b = [1]

pointer_a = 0
pointer_b = 0
answer = []

while length_a != pointer_a or length_b != pointer_b:
    if pointer_a == length_a:
        answer.append(b[pointer_b])
        pointer_b += 1
    elif pointer_b == length_b:
        answer.append(a[pointer_a])
        pointer_a += 1
    else:
        
        if a[pointer_a] > b[pointer_b]:
            answer.append(b[pointer_b])
            pointer_b += 1
        elif a[pointer_a] <= b[pointer_b]:
            answer.append(a[pointer_a])
            pointer_a += 1

print(*answer)
