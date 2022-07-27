"""
 *packageName    : 
 * fileName       : 1063_백준_킹_S3
 * author         : ipeac
 * date           : 2022-07-27
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-27        ipeac       최초 생성
 """
king_position, stone_position, n = input().split()
king_position = list(map(int, [king_position[1], ord(king_position[0]) - 64]))
stone_position = list(map(int, [stone_position[1], ord(stone_position[0]) - 64]))

move = {'R': [0, 1], 'L': [0, -1], 'B': [-1, 0], 'T': [1, 0], 'RT': [1, 1], 'LT': [1, -1], 'RB': [-1, 1],
        'LB': [-1, -1]}

n = int(n)

king_move_arr = [input() for _ in range(n)]


def move_def(value):
    # 행 열 이동
    nx, ny = king_position[0] + move[value][0], king_position[1] + move[value][1]
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        # 돌의 위치와 동일하다면 돌을 킹이 움직인 방향과 같이 맞춤
        if nx == stone_position[0] and ny == stone_position[1]:
            # 돌의 포지션 체크
            nx_stone, ny_stone = stone_position[0] + move[value][0], stone_position[1] + move[value][1]

            if 1 <= nx_stone <= 8 and 1 <= ny_stone <= 8:
                king_position[0], king_position[1] = nx, ny
                stone_position[0], stone_position[1] = nx_stone, ny_stone
        # 킹만 고려함
        else:
            king_position[0], king_position[1] = nx, ny


for value in king_move_arr:
    move_def(value)

print(chr(king_position[1] + 64) + str(king_position[0]))
print(chr(stone_position[1] + 64) + str(stone_position[0]))
