"""
 *packageName    : 
 * fileName       : 17690_r회문
 * author         : qkrtkdwns3410
 * date           : 2022-09-07
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-07        qkrtkdwns3410       최초 생성
 """

# 회문 0  유사회문 1 그외 2
T = int(input())  # 문자열의 개수
t_arr = []
for _ in range(T):
    t_arr.append(input())

def is_palindrome_slice(string, left, right):
    while left < right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def is_palindrome(string):
    left = 0
    right = len(string) - 1
    
    if string == string[::-1]:
        return 0
    else:
        while left < right:
            if string[left] != string[right]:
                left_slice_return = is_palindrome_slice(string, left + 1, right)
                right_slice_return = is_palindrome_slice(string, left, right - 1)
                
                if left_slice_return or right_slice_return:
                    return 1
                else:
                    return 2
            else:
                left += 1
                right -= 1

for string in t_arr:
    print(is_palindrome(string))
