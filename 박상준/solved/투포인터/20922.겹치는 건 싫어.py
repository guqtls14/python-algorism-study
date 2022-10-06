"""
 *packageName    : 
 * fileName       : 20922.겹치는 건 싫어
 * author         : ipeac
 * date           : 2022-10-04
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-04        ipeac       최초 생성
 """
# n, k = 9, 2
n, k = map(int, input().split())
# a = [3, 2, 5, 5, 6, 4, 4, 5, 7]
a = list(map(int, input().split()))

# 도현이를 위해 같은 원소가 k개 이하로 들어 있는 최장 연속 부분 수열의 길이를 구하려고 한다.
left, right = 0, 0

counter = [0] * (max(a) + 1)
answer = 0
while right < n:
    print(f"right : {right}")
    if counter[a[right]] < k:
        print(f"counter right: {counter[a[right]]}")
        counter[a[right]] += 1
        right += 1
    else:  # k 값 초과가 되어버리면 안됨 left 값을
        print(f"counter left: {counter[a[left]]}")
        counter[a[left]] -= 1
        
        left += 1
    answer = max(answer, right - left)
print(answer)
