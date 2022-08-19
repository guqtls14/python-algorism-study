"""
 *packageName    : 
 * fileName       : 124나라
 * author         : qkrtkdwns3410
 * date           : 2022-08-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-19        qkrtkdwns3410       최초 생성
 """
n_arr = ['4', '1', '2']


def solution(n):
    print("n : %s " % n)
    answer = ''
    # 몫
    moc = n // 3
    # 나머지
    remain = n % 3
    
    if n == 1:
        answer = 1
        return answer
    elif n == 2:
        answer = 2
        return answer
    elif n == 3:
        answer = 4
        return answer
    
    while n > 0:
        # 3으로 나누어 떨어짐
        if n % 3 == 0:
            answer += n_arr[n % 3]  # 4
            n //= 3
            n -= 1
            pass
        # 3의 나머지가 존재함
        else:
            answer += n_arr[n % 3]  # 1 , 2
            n //= 3
            pass
    answer = answer[::-1]
    print("answer : %s " % answer)
    return answer


# solution(1)
# print("==========================================")
# solution(2)
# print("==========================================")
# solution(3)
# print("==========================================")
# solution(4)
# print("==========================================")
solution(5)
print("==========================================")
solution(6)
print("==========================================")
solution(7)
print("==========================================")
solution(8)
print("==========================================")
solution(9)
print("==========================================")
solution(10)
print("==========================================")
