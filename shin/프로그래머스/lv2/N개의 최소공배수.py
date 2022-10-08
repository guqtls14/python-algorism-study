from math import gcd


def solution(arr):
    def lcm(x, y):
        return x * y // gcd(x, y)

    while True:
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr) == 1:
            return arr[0]

arr=[2,6,8,14]
print(solution(arr))

# 최소공배수:
# 최소공배수는 x와 y의 공통된 배수 가운데 최소값을 의미합니다.
#  더 쉽게 말해서, 최소공배수는 주어진 수인 x,y의 곱에서 x,y의 최대공약수를 나누어 준 것과 같습니다. 
#  즉, 유클리드 호제법을 사용해 최대공약수를 구한 다음, x와 y의 곱한 값을 나눠주면 최소공배수를 구할 수 있습니다.

# N개의 최소공배수
# 최소공배수는 2개의 수를 대상으로 실행하기 때문에 주어진 수가 3개 이상일 때, 막막해 보이지만 해결방법은 간단합니다.
# 먼저 2개의 수에 대해 최소공배수를 구한 다음, 그 값과 계산하지 않은 값들 중 1개를 선택해 다시 최소공배수를 구합니다.
# 이렇게 모든 수에 대해 최소공배수를 구하면 N개의 최소공배수를 구할 수 있습니다.

# https://brownbears.tistory.com/454