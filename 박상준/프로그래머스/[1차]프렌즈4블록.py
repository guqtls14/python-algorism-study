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
import pprint


def solution(m, n, board):
    print(f"m,n,board : {m, n, board}")
    answer = 0
    graph = []
    for value in board:
        li = list(value)
        graph.append(li)
    pprint.pprint(graph)
    while True:
        save = []
        
        x = len(graph)
        y = len(graph[0])
        for i in range(x - 1):
            for j in range(y - 1):
                chk = True
                print(f"i, j : {i, j}")
                
                # 빈공간은 패스함
                if graph[i][j] == []:
                    continue
                    pass
                if board[i + 1][j]
                
                if chk:
                    save.append([i, j])
        
        # 지울 친구가 존재한다면
        if save:
            print(f"save : {save}")
            for value in save:
                board[value[0]][value[1]], board[value[0] + 1][value[1]], board[value[0] + 1][value[1] + 1], board[value[0]][
                    value[1] + 1] = [], [], [], []
        
        if not save:
            break
    
    return answer


# m 판의 높이 (x)|| n 폭(y) || 판의 배치 정보 (board)
solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])
