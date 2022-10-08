def solution(citations):
    # answer = 0
    for i in range(len(citations)):
        answer=0
        for j in range(len(citations)):
            if citations[i] <= citations[j]:
                answer += 1
        if answer == citations[i]:

            return answer

li=[6,6,6,6,6,1]

print(solution(li))