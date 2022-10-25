def solution(progresses, speeds):
    answer = []
    time=0
    answerelement=0


    while progresses:
        if progresses[0]+speeds[0]*time >=100:
            progresses.pop(0)
            speeds.pop(0)
            answerelement+=1
            # answer.append(answerelement)
        else:
            if answerelement>=1:
                answer.append(answerelement)
                answerelement=0
            
            time+=1
    answer.append(answerelement)
    return answer

progresses=[93, 30, 55]
speeds=[1, 30, 5]

print(solution(progresses,speeds))