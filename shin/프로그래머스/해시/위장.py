# from collections import Counter
# from functools import reduce

# def solution(clothes):
#     # 1. 의상 종류별 Counter를 만든다.
#     counter = Counter([type for clothe, type in clothes])

#     # 2. 모든 종류의 count + 1을 누적하여 곱해준다
#     answer = reduce(lambda acc, cur: acc*(cur+1), counter.values(), 1) - 1
#     return answer


# def solution(clothes):
#     closet = {}
#     answer = 1
    
#     # 같은 종류의 옷끼리 묶어서 사전에 저장
#     for cloth in clothes:
#         if cloth[1] in closet.keys():
#             closet[cloth[1]].append(cloth[0])
#         else:
#             closet[cloth[1]] = [cloth[0]]
    
#     # 경우의 수 구하기            
#     for value in closet.values():
#         # 아무것도 안입는경우 +1
#         answer *= len(value) + 1
    
#     # 아무것도 입지 않은 경우 하나 제외(전체다)
#     return answer-1

# print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
# print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))


# https://velog.io/@devjuun_s/%EC%9C%84%EC%9E%A5-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4
# https://latte-is-horse.tistory.com/140

def solution(clothes):
    tmp={}
    answer=1
    for i in clothes:
        if i[1] in tmp:
            tmp[i[1]].append(i[0])
        else:
            tmp[i[1]]=[i[0]]
    print(tmp)
    for i in tmp.values():
        answer *= len(i)+1
    return answer-1

# print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))