n=int(input())
for _ in range(n):
    li=list(map(str, input()))
    if (int(''.join(li[4:6])) < int(1) or int(''.join(li[4:6])) >= int(12)):
        print('#{} {}'.format(_+1,-1))
        continue
    if ''.join(li[4:6]) == '02':
        if int(''.join(li[-2:])) <=int(1) or int(''.join(li[-2:])) >= int(29):
            print('#{} {}'.format(_+1,-1))
            continue
    if ''.join(li[4:6]) == '01' or ''.join(li[4:6])  == '03' or ''.join(li[4:6])  == '05' or ''.join(li[4:6])  == '07' or ''.join(li[4:6]) == '08' or ''.join(li[4:6]) == '10' or ''.join(li[4:6])  == '12':
        if int(''.join(li[-2:])) <1 or int(''.join(li[-2:])) >= 32:
            print('#{} {}'.format(_+1,-1))
            continue
    if ''.join(li[4:6]) == '04' or ''.join(li[4:6])  == '06' or ''.join(li[4:6])  == '09' or ''.join(li[4:6])  == '11':
        if int(''.join(li[-2:])) <1 or int(''.join(li[-2:])) >= 31:
            print('#{} {}'.format(_+1,-1))
            continue
    print('#{} {}'.format(_+1,''.join(li[0:4])+'/'+''.join(li[4:6])+'/'+''.join(li[-2:])))


# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
# for test_case in range(1, T + 1):
#    case = str(input())
#    year = case[0:4]
#    month = case[4:6]
#    day = case[6:8]
   
#    answer = ''
#    if 0 < int(month) < 13 and 0 < int(day) <= days[int(month)]:
#        answer = year + '/' + month + '/' + day
#    else:
#        answer += '-1'
# ​
#    print("#" + str(test_case) + " " + answer)

# https://sohee-dev.tistory.com/17