from collections import Counter

def solution(participant, completion):
    answer = ''
    counter_a = Counter(participant)
    print(f"counter_a : {counter_a}")
    counter_b = Counter(completion)
    print(f"counter_b : {counter_b}")
    count = counter_a - counter_b
    print(f"count : {count}")
    
    for name in count.keys():
        answer = name
    return answer
    
         
    

participant=["mislav", "stanko", "mislav", "ana"]
completion=["stanko", "ana", "mislav"]

print(solution(participant, completion))

# https://coding-grandpa.tistory.com/85
# https://yunaaaas.tistory.com/46