"""
 *packageName    : 
 * fileName       : 영어 끝말잇기
 * author         : ipeac
 * date           : 2022-09-05
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-05        ipeac       최초 생성
 """

def solution(n, words):
    answer = []
    for i, word in enumerate(words):
        if i >= 1 and (last_word != word[0] or word in words[:i]):
            print(f"i : {i}")
            answer.append((i % n) + 1)
            answer.append((i // n) + 1)
            return answer
        last_word = word[-1]
    return [0, 0]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
