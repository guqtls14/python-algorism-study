"""
 *packageName    : 
 * fileName       : 20436.ZOAC3
 * author         : ipeac
 * date           : 2022-10-02
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-02        ipeac       최초 생성
 """
keyboard = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
    , ['z', 'x', 'c', 'v', 'b', 'n', 'm']]

za = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v']  # 자음
ans = 0

def now_which(hand):
    for i, key, in enumerate(keyboard):
        if hand in key:
            x, y = i, key.index(hand),
            return x, y

# 첫번째 위치들
left, right = map(str, input().split())
target_word = input()

for word in target_word:
    # 이미 그 자리에 있는 경우 생각
    if left == word or right == word:
        ans += 1
    else:
        left_x_y, right_x_y, target_x_y = now_which(left), now_which(right), now_which(word)
        left_dist = abs(left_x_y[0] - target_x_y[0]) + abs(left_x_y[1] - target_x_y[1])
        right_dist = abs(right_x_y[0] - target_x_y[0]) + abs(right_x_y[1] - target_x_y[1])
        # 자음인지 확인 먼저
        if word in za:
            left = word
            ans += left_dist + 1
        else:
            right = word
            ans += right_dist + 1
print(ans)
