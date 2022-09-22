n=int(input())
li=list(map(str,input().split()))

list=[]
def reverse(x):
    return x[::-1]

# 소수 판별 함수(2이상의 자연수에 대하여)
def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x+1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
         
    return True

for i in li:
    number = reverse(i)
    if is_prime_number(int(number)):
        print(int(number),end=' ')
# print(*list)
