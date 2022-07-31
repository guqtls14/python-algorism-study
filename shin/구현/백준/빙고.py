# import sys
# input = int(input())

# 숫자들의 위치 기록
board = dict()
check = [[0]*5 for i in range(5)]
for i in range(5):
    a = list(map(int,input().split()))

    for j in range(5):
        board[a[j]] = (i,j)
# print(board)
tick = 0
for _ in range(5):
    a = list(map(int,input().split()))
    # print('a: ',a)
    for i in range(5):
        tick += 1
        
        # 불린 숫자가 보드에 있을 경우
        if a[i] in board:
            # print('a[i]: ',a[i])
            # 딕셔너리를 이용해 기록
            # print('board: ',board)
            # print('board key: ',board[a[i]])
            # print('board[]: ',check[board[a[i]][0]][board[a[i]][1]])
            check[board[a[i]][0]][board[a[i]][1]] = 1
            # print('check: ',check)
            # 빙고 세주기
            bingo = 0
            for j in range(5):
                if sum(check[j]) == 5:
                    bingo+=1
                # 세로
                sum_vertical = 0
                for i in range(5):
                    sum_vertical += check[i][j]
                    if sum_vertical == 5:
                        bingo+=1
                # if sum([k[j] for k in check]) == 5:
                #     bingo+=1
            if check[0][4]+check[1][3]+check[2][2]+check[3][1]+check[4][0] == 5:
                bingo+=1
            if check[0][0]+check[1][1]+check[2][2]+check[3][3]+check[4][4] == 5:
                bingo+=1
                
            if bingo >= 3:
                print(tick)
                # sys.exit()
                exit()
