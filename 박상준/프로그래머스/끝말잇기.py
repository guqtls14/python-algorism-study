"""
 *packageName    : 
 * fileName       : 끝말잇기
 * author         : ipeac
 * date           : 2022-08-21
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-21        ipeac       최초 생성
 """


def solution(n, words):
    print("n : %s " % n)
    print("words : %s " % words)
    
    answer = []
    # 몇번째 사람이 몇번 째 단어 외침에서 통과하지 못했는지..
    for index in range(1, len(words)):
        if words[index][0] != words[index - 1][-1]:
            answer = [index % n + 1, index // n + 1]
            return answer
            pass
        for index2 in range(index):
            if words[index] in words[:index]:
                answer = [index % n + 1, index // n + 1]
                return answer
                pass
    answer = [0, 0]
    return answer


solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])
print("==========================================")
solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference",
             "estimate", "executive"])
print("==========================================")
solution(2, ["hello", "one", "even", "never", "now", "world", "draw"])
print("==========================================")
