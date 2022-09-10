"""
 *packageName    : 
 * fileName       : 1972.놀라운 문자열
 * author         : qkrtkdwns3410
 * date           : 2022-09-10
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-10        qkrtkdwns3410       최초 생성
 """
string_list = []

while True:
    i_p = input()
    if i_p == '*':
        break
    string_list.append(i_p)

for value in string_list:
    k = value
    for i in range(1, len(k) - 1):
        check = set()
        for j in range(len(k) - i):
            pairs = k[j] + k[i + j]
            if pairs in check:
                print(k, "is NOT surprising.")
                break
            else:
                check.add(pairs)
        else:  # for 문이 다 돈 경우
            continue
        break
    else:
        print(k, "is surprising.")
