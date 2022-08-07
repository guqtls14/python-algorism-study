"""
 *packageName    : 
 * fileName       : 3번
 * author         : jihye94
 * date           : 2022-08-06
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-06        jihye94       최초 생성
 """


def solution(k, dungeons):
    print("k : %s " % k)
    print("dungeons : %s " % dungeons)
    sorted_dungeouns = sorted(dungeons, key=lambda x: [-x[0], x[1]])
    print("sorted_dungeouns : %s " % sorted_dungeouns)
    list_for = []
    for index, item in enumerate(sorted_dungeouns):
        list_for.append([index, (item[0] - item[1])])
        print("list_for : %s " % list_for)
    count = 0
    
    sorted_list_for = sorted(list_for, key=lambda x: x[1])
    for item in sorted_list_for:
        if item[0] <= k:
            count += 1
    print(count)
    return count


solution(80, [[80, 20], [50, 40], [30, 10]])
print("==========================================")
