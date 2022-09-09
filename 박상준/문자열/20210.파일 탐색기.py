"""
 *packageName    : 
 * fileName       : 20210.파일 탐색기
 * author         : qkrtkdwns3410
 * date           : 2022-09-09
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-09        qkrtkdwns3410       최초 생성
 """
# n = int(input())
# string = []
# for _ in range(n):
#     string.append(input())
n = 8
string = ['Foo1Bar', 'Foo12Bar', 'Foo3bar', 'Fo6Bar', 'Foo12Bar', 'Foo00012Bar', 'Foo3Bar', 'foo4bar', 'FOOBAR']

def to_list(word):
    li = list(word)
    i = 0
    while i < len(li):
        if li[i].isdigit():
            end = i
            while end < len(li) and li[end].isdigit():
                end += 1
            li[i:end] = [''.join(li[i:end])]

def solution(n, string):
    pass

solution(n, string)
