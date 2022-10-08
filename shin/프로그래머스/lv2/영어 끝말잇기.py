def solution(n, words):
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i] :
            # 순서가 반복되면서 해당 반복의 숫자를 구할때는 나머지와 몫을 이용
            return [(i%n)+1, (i//n)+1]
    else:
        return [0,0]

# def solution(n, words):
#     answer = [0,0]

#     cnt = 0  # 탈락번호,차례 계산할 변수
#     checks = []  # 나온 단어 확인할 리스트
#     checks.append(words[0])
#     for i in range(1, len(words)):  # 단어 순회하면서
#         cnt += 1
#         # 아직 안나온 단어이면서 & 앞 단어의 마지막 알파벳과 일치하면 checks 리스트에 넣음 (pass)
#         if words[i] not in checks and list(words[i-1])[-1] == list(words[i])[0]:
#             checks.append(words[i])
#         else:  # (fail)
#             answer[0] = cnt%n +1  # 탈락번호
#             answer[1] = cnt//n +1  # 탈락차례
#             break

#     return answer

n=2
# word=["tank", "kick", "know", "tank", "land", "dream", "mother", "robot","wheel"]
word=["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n,word))

# https://velog.io/@insutance/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Python-%EC%98%81%EC%96%B4-%EB%81%9D%EB%A7%90%EC%9E%87%EA%B8%B0