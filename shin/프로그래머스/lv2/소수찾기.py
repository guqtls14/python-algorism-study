from itertools import permutations

def solution(numbers):
    answer = []              
        
    # numbers를 하나씩 자른 것
    nums = [n for n in numbers]
    per = []                                      
    for i in range(1, len(numbers)+1):            # numbers의 각 숫자들을 순열로 모든 경우 만들기
        per += list(permutations(nums, i))        # i개씩 순열조합
        print(per)
    # for i in per:
    #     print('i: ',i)
    new_nums = [int(("").join(p)) for p in per]   # 각 순열조합을 하나의 int형 숫자로 변환


    for n in new_nums:                            # 모든 int형 숫자에 대해 소수인지 판별
        if n < 2:                                 # 2보다 작은 1,0의 경우 소수 아님
            continue
        # 반복문이끝나고 check와같은 boolean값이없으면 무조건적으로 실행이되는데 조건을 함으로써 특정 케이스만 코드가 실행되게 해줌
        check = True            
        for i in range(2,int(n**0.5) + 1):        # n의 제곱근 보다 작은 숫자까지만 나눗셈
            # n의 제곱근을 기준으로, 제곱근보다 작은 수들 중에 약수가 없다면, 제곱근보다 큰 수들은 n의 약수가 아니다
            if n % i == 0:                        # 하나라도 나눠떨어진다면 소수 아님!
                check = False
                break
        if check:
            answer.append(n) 
  
    # set을 하는이유는 중복을 없애기위함
    return len(set(answer))
# https://dev-note-97.tistory.com/99
# https://veggie-garden.tistory.com/17

# join
# https://blockdmask.tistory.com/468
# 순열,조합 라이브러리
# https://seu11ee.tistory.com/5
print(solution('011'))

