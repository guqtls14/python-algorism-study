# i라는 숫자에 3 6 9 가 들어간 수 만큼 -출력, 띄어쓰기 없이
# 그 외에는 일반 숫자 출력

# T = int(input())
# for i in range(1, T+1): # 1 ~ 100

#     i = str(i)
#     clap = i.count('3') + i.count('6') + i.count('9')

#     if clap == 0:
#         print(i, end=' ')
#     else:
#         print("-" * clap, end=' ')
# count:문자열과 리스트에서 원소의갯수(정수)를반환

N = int(input())
result = ''

for test_case in range(1, N + 1):
    num = str(test_case)
    cnt = 0
    
    if '3' in num:
        cnt += num.count('3')
    if '6' in num:
        cnt += num.count('6')
    if '9' in num:
        cnt += num.count('9')
        
    if(cnt==0):
        result += num
    else:
        for i in range(cnt):
            result += '-'
    # 한칸 띄어쓰기
    result += ' '

print(result)