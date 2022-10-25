
# 1번째 풀이
# from collections import Counter

# def solution(participant, completion):
#     answer = ''
#     counter_a = Counter(participant)

#     counter_b = Counter(completion)

#     count = counter_a - counter_b
#     print(f"count : {count}")
    
#     for name in count.keys():
#         answer = name
#     return answer
    
         
    

# participant=["mislav", "stanko", "mislav", "ana"]
# completion=["stanko", "ana", "mislav"]

# print(solution(participant, completion))

# # https://coding-grandpa.tistory.com/85
# # https://yunaaaas.tistory.com/46

# 2번째풀이
# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     print('p',participant)
#     print('c',completion)
#     for p,c in zip(participant, completion):
#         print(p,c)
#         if p != c:
#             return p
#     return participant.pop()

# participant=["mislav", "stanko", "mislav", "ana"]
# completion=["stanko", "ana", "mislav"]


# print(solution(participant, completion))
# zip:두 이터러블객체에서 같은 인덱스끼리 튜플을 만들어줌!
# https://velog.io/@matisse/%EC%99%84%EC%A3%BC%ED%95%98%EC%A7%80-%EB%AA%BB%ED%95%9C-%EC%84%A0%EC%88%98-python
# https://www.daleseo.com/python-zip/

# 3번째풀이
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(participant)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant) -1]



participant=["mislav", "stanko", "mislav", "ana"]
completion=["stanko", "ana", "mislav"]


print(solution(participant, completion))