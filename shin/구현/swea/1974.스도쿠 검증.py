
def check(a):
    for i in range(9):
        ch1=[0]*10
        ch2=[0]*10
        for j in range(9):
            ch1[a[i][j]]=1
            ch2[a[j][i]]=1
     
        if sum(ch1) != 9 or sum(ch2) !=9:
            return False
    for i in range(3):
        for j in range(3):
            ch3=[0] * 10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]]=1
            if sum(ch3) != 9:
                return False
    return True
a=[list(map(int, input().split())) for _ in range(9)]

if check(a):
    print(1)
else:
    print(0)

# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):

#     def check(a):
#         for i in range(9):
#             ch1=[0]*10
#             ch2=[0]*10
#             for j in range(9):
#                 ch1[a[i][j]]=1
#                 ch2[a[j][i]]=1

#             if sum(ch1) != 9 or sum(ch2) !=9:
#                 return False
#         for i in range(3):
#             for j in range(3):
#                 ch3=[0] * 10
#                 for k in range(3):
#                     for s in range(3):
#                         ch3[a[i*3+k][j*3+s]]=1
#                 if sum(ch3) != 9:
#                     return False
#         return True
#     a=[list(map(int, input().split())) for _ in range(9)]

#     if check(a):
#         print('#{} {}',format(test_case,1))
#     else:
#         print('#{} {}',format(test_case,0))

# https://jennnn.tistory.com/21?category=949329