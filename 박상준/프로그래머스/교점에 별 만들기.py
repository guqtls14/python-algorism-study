"""
 *packageName    : 
 * fileName       : 교점에 별 만들기
 * author         : ipeac
 * date           : 2022-09-14
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-14        ipeac       최초 생성
 """


def solution(line):
    star_list = []
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            a, b, e = line[i]
            c, d, f = line[j]
            if a * d - b * c != 0:
                x, y = (b * f - e * d) / (a * d - b * c), (e * c - a * f) / (a * d - b * c)
                if x.is_integer() and y.is_integer():
                    x, y = int(x), int(y)
                    if (x, y) not in star_list:
                        star_list.append((x, y))
    x_min, x_max, y_min, y_max = min(star_list)[0], max(star_list)[0], min(star_list, key=lambda x: x[1])[1], max(star_list, key=lambda x: x[1])[1]
    star = [['.'] * (abs(x_max - x_min) + 1) for _ in range((abs(y_max - y_min) + 1))]
    for s in star_list:
        a, b = s
        x, y = abs(y_max - b), abs(x_min - a)
        star[x][y] = '*'
    for i, v in enumerate(star):
        star[i] = ''.join(v)
    return star


# print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]])
# solution([[1, -1, 0], [2, -1, 0]])
# solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]])
