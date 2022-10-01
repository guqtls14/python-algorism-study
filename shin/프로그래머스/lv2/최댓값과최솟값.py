
def solution(s):
    arr = list(map(int, s.split(' ')))
    print(arr)
    return str(min(arr)) + " " + str(max(arr))

word='-1 -2 -3 -4'
print(solution(word))