"""
 *packageName    : 
 * fileName       : 13022.늑대와 올바른 단어
 * author         : (qkrtkdwns3410
 * date           : 2022-09-12
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-12        qkrtkdwns3410       최초 생성
 """
string = 'wowollff'
c = 1
w_count = 0
o_count = 0
l_count = 0
f_count = 0

for i, v in enumerate(string):
    if v == 'w':
        w_count += 1
        if l_count != f_count:
            c = 0
            break
    elif v == 'o':
        o_count += 1
        if w_count < o_count:
            c = 0
            break
    elif v == 'l':
        l_count += 1
        if o_count < l_count or w_count != o_count:
            c = 0
            break
    elif v == 'f':
        f_count += 1
        if l_count < f_count or w_count != o_count or o_count != l_count:
            c = 0
            break
if w_count == o_count and o_count == l_count and l_count == f_count and c == 1:
    print(1)
else:
    print(c)
