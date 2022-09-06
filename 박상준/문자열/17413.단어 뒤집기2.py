"""
 *packageName    : 
 * fileName       : 17413.단어 뒤집기2
 * author         : qkrtkdwns3410
 * date           : 2022-09-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-06        qkrtkdwns3410       최초 생성
 """

s = input()

def solution(s):
    # input temp
    tmp = []
    flag = False
    
    for string in s:
        # flow
        if string.isspace():
            tmp.reverse()
            for v in tmp:
                print(v, end="")
            print(" ", end="")
            tmp = []
            continue
        if string == '<':
            tmp.reverse()
            for v in tmp:
                print(v, end="")
            tmp = []
            
            flag = True
            print('<', end="")
            continue
        
        if string == '>':
            flag = False
            print('>', end="")
            continue
        if flag:
            print(string, end="")
            continue
        
        # LOGIC
        if not flag:
            tmp.append(string)
    tmp.reverse()
    for v in tmp:
        print(v, end="")
    print()

solution(s)

solution("baekjoon online judge")
solution("<open>tag<close>")
solution("<ab cd>ef gh<ij kl>")
solution("one1 two2 three3 4fourr 5five 6six")
solution("<int><max>2147483647<long long><max>9223372036854775807")
solution("<   space   >space space space<    spa   c e>")
