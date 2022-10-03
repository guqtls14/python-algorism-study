def solution(brown, yellow):
    answer = []
    
    sum_by = brown + yellow
    
    sum_list = []
    # 해당 값의 약수만 담습니다.
    for i in range(1, sum_by + 1):
        if sum_by % i == 0:
            sum_list.append(i)
    # 홀수개인 경우
    if len(sum_list) % 2 != 0:
        mid_value = sum_list[len(sum_list) // 2]
        sum_list.insert(len(sum_list) // 2, mid_value)
    for i in range(len(sum_list) // 2):
        width = sum_list[-i - 1]
        height = sum_list[i]
        
        if brown == width * 2 + 2 * (height - 2):
            return [width, height]
    
    return answer