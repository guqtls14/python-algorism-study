"""
 *packageName    : 
 * fileName       : 14467_소가 길을 건너간 이유1_ S5
 * author         : jihye94
 * date           : 2022-07-29
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-29        jihye94       최초 생성
 """
graph = {}
graph_ans = [[0] * 5 for _ in range(5)]
for i in range(5):
    line = list(map(int, input().split()))
    for j, value in enumerate(line):
        graph[value] = (i, j)
ans = 0
# 밸류값 설정
for i in range(5):
    
    line = list(map(int, input().split()))
    for value in line:
        bingo_cnt = 0
        graph_ans[graph[value][0]][graph[value][1]] = 1
        ans += 1
        
        # 대각선 체크 ( 왼 _ 오) || (오_왼)
        side_sum_lr = 0
        side_sum_rl = 0
        
        for i in range(5):
            side_sum_lr += graph_ans[i][i]
            side_sum_rl += graph_ans[i][4 - i]
        
        if side_sum_lr == 5:
            bingo_cnt += 1
        
        if side_sum_rl == 5:
            bingo_cnt += 1
        
        # 가로 체크
        for line in graph_ans:
            if sum(line) == 5:
                bingo_cnt += 1
                
                if bingo_cnt >= 3:
                    print(ans)
                    exit()
        # 세로 체크
        for k in range(5):
            sum_vertical = 0
            for j in range(5):
                
                sum_vertical += graph_ans[j][k]
                if sum_vertical == 5:
                    bingo_cnt += 1
                    
                    if bingo_cnt >= 3:
                        print(ans)
                        exit(0)
