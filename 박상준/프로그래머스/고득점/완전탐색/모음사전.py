"""
 *packageName    : 
 * fileName       : 모음사전
 * author         : ipeac
 * date           : 2022-10-11
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-11        ipeac       최초 생성
 """
# -*- coding: utf-8 -*-

"""
word	result
"AAAAE"	6
"AAAE"	10
"I"	1563
"EIO"	1189
"""

def solution(word):
    answer = set()
    
    string_arr = ["", "A", "E", "I", "O", "U"]
    
    def make_word(n, string):
        if n == 0:
            answer.add(string)
            return
        
        for i in range(len(string_arr)):
            make_word(n - 1, string + string_arr[i])
    
    make_word(5, "")
    answer = list(answer)
    answer.sort()
    
    for idx, value in enumerate(answer):
        if value == word:
            return idx

print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))
