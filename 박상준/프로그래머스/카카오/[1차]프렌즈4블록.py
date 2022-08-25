"""
 *packageName    : 
 * fileName       : [1차]프렌즈4블록
 * author         : ipeac
 * date           : 2022-08-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-23        ipeac       최초 생성
 """


def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])
    
    cnt = 0
    save = set()
    
    while True:
        
        x = len(board)
        y = len(board[0])
        for i in range(x - 1):
            for j in range(y - 1):
                t = board[i][j]
                
                # 빈공간은 패스함
                if not board[i][j]:
                    continue
                
                if board[i + 1][j] == t and board[i + 1][j + 1] == t and board[i][j + 1] == t:
                    save.add((i, j))
                    save.add((i + 1, j))
                    save.add((i + 1, j + 1))
                    save.add((i, j + 1))
        
        # 지울 친구가 존재한다면
        if save:
            cnt += len(save)
            
            for i, j in save:
                board[i][j] = []
            save = set()
        else:
            return cnt
        
        #
        while True:
            moved = 0
            for i in range(m - 1):
                for j in range(n):
                    if board[i][j] and board[i + 1][j] == []:
                        board[i + 1][j] = board[i][j]
                        board[i][j] = []
                        moved += 1
            if moved == 0:
                break


# m 판의 높이 (x)|| n 폭(y) || 판의 배치 정보 (board)
solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])
