"""
 *packageName    : 
 * fileName       : 1331_백준_나이트 투어_S5
 * author         : jihye94
 * date           : 2022-07-28
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-28        jihye94       최초 생성
 """
chess_arr = [input() for _ in range(36)]

for i in range(35):
    cha1 = abs((ord(chess_arr[i][0]) - 64) - (ord(chess_arr[i + 1][0]) - 64))
    cha2 = abs(int(chess_arr[i][1]) - int(chess_arr[i + 1][1]))

    if cha1 == 1 and cha2 == 2:
        pass
    elif cha1 == 2 and cha2 == 1:
        pass
    else:
        print("Invalid")
        exit(0)
    if i == 34:
        cha1 = abs((ord(chess_arr[i + 1][0]) - 64) - (ord(chess_arr[0][0]) - 64))
        cha2 = abs(int(chess_arr[i + 1][1]) - int(chess_arr[0][1]))
        if (cha1 == 1 and cha2 == 2) or (cha1 == 2 and cha2 == 1):
            pass
        else:
            print("Invalid")
            exit(0)

print("Valid" if len(set(chess_arr)) == 36 else "Invalid")
