# # def solution(priorities, location):
# #     answer = 0
# #     answerIndex=priorities[location]
# #     while answerIndex in priorities:
# #         print('answer: ',answerIndex)
# #         tmp = priorities.pop(0) 
# #         if tmp >= max(priorities):
# #             answer+=1
# #             if tmp == answerIndex:
# #                 return answer
# #             else:
# #                 continue
# #         else:
# #             priorities.append(tmp)
# #     # return answer

from collections import deque
def solution(priorities, location):
    answer=0
 
    d = deque([(v,i) for i,v in enumerate(priorities)])

  
    while len(d):
        item = d.popleft()
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            # 깉은 문자에대해서 구별되는값인지 확인
            if item[1] == location:
                break
    return answer

# priorities=[2, 1, 3, 2]
priorities=[1, 1, 9, 1, 1, 1]
location=0
print(solution(priorities,location))

# 참고
# https://eda-ai-lab.tistory.com/461

# matrix = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]

# for r, row in enumerate(matrix):
#     print('r',r,'row',row)
#     for c, letter in enumerate(row):
#           print(r, c, letter)