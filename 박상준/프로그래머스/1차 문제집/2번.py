"""
 *packageName    : 
 * fileName       : 2번
 * author         : ipeac
 * date           : 2022-08-22
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-22        ipeac       최초 생성
 """


def solution(want, number, discount):
    dic = dict()
    for i, item in enumerate(want):
        dic[item] = number[i]
    print("==========================================")
    print("dic : %s " % dic)
    print("==========================================")
    answer = 0
    
    for i in range(len(discount) - 9):
        dc = discount[i:i + 10]
        print(f"dc : {dc}")
        
        cnt = 0
        for w in want:
            if dic[w] == dc.count(w):
                cnt += 1
        if cnt == len(want):
            answer += 1
    print(f"answer : {answer}")
    
    return answer


solution(["banana", "apple", "rice", "pork", "pot"], [1, 1, 1, 1, 1],
         ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])
