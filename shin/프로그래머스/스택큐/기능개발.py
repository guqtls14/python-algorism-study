# def solution(progresses, speeds):
    
#     answer = []
#     time = 0
#     count = 0
    
#     while len(progresses)> 0:
#         if (progresses[0] + time*speeds[0]) >= 100: 
#             progresses.pop(0)
#             speeds.pop(0)
#             count += 1
            
#         else:
#             if count > 0:
#                 answer.append(count)
#                 count = 0
#             time += 1
#     answer.append(count)
#     return answer

def solution(progresses, speeds):
    answer = []
    time=0
    cnt=0
    
    while len(progresses) > 0:
        if progresses[0] + time * speeds[0] >=100:
            progresses.pop(0)
            speeds.pop(0)
            cnt+=1
        else:
            if cnt >0:
                answer.append(cnt)
                cnt=0
            time+=1
    answer.append(cnt)
    return answer
li=[93,30,55]
speed=[1,30,5]
print(solution(li,speed))



