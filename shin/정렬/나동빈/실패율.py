# def solution(N,stages):
#     result={}
#     denominator = len(stages)
#     for stage in range(1,N+1):
#         if denominator != 0:
#             count = stages.count(stage)
#             result[stage] = count / denominator
#             denominator -= count
#         else:
#             result[stage] = 0
#     print(result)

#     return sorted(result,key=lambda x : result[x],reverse=True) # value기준 정렬,key return



def solution(N, stages):
    answer = {}
    depen=len(stages)
    for i in range(1,N+1):
        if depen != 0:
            count=stages.count(i)
            answer[i]=count/depen
            depen-=count
        else:
            answer[i] = 0
    return sorted(answer,key=lambda x:answer[x],reverse=True)

print(solution(5,[2,1,2,6,2,4,3,3]))

# https://velog.io/@kylexid/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-%EB%94%95%EC%85%94%EB%84%88%EB%A6%AC-%EC%9E%90%EB%A3%8C-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0