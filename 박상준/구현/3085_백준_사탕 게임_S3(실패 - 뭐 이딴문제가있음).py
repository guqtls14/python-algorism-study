"""
 *packageName    : 
 * fileName       : 3085_백준_사탕 게임_S3
 * author         : jihye94
 * date           : 2022-07-27
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-27        jihye94       최초 생성
 """
# 보드의 크기
n = int(input())

n_arr = [list(map(str, input())) for _ in range(n)]


def count_row_col():
    # 행 카운트
    row_max_cnt = 1

    for i in range(n):

        cnt = 1
        for j in range(1, n):

            if n_arr[i][j] == n_arr[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
        row_max_cnt = max(row_max_cnt, cnt)

    # 열 카운트

    col_max_cnt = 1

    for j in range(n):
        cnt = 1
        for i in range(1, n):

            if n_arr[i][j] == n_arr[i - 1][j]:
                cnt += 1
            else:
                cnt = 1
        col_max_cnt = max(col_max_cnt, cnt)
    return max(col_max_cnt, row_max_cnt)


ans = 0
steps = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for i in range(n):
    for j in range(n):

        for k in range(4):
            nx, ny = i + steps[k][0], j + steps[k][1]
            if 0 <= nx < n and 0 <= ny < n:
                if n_arr[i][j] != n_arr[nx][ny]:
                    n_arr[nx][ny], n_arr[i][j] = n_arr[i][j], n_arr[nx][ny]
                    ans = max(ans, count_row_col())
                    n_arr[nx][ny], n_arr[i][j] = n_arr[i][j], n_arr[nx][ny]

print(ans)

# https://data-flower.tistory.com/97
