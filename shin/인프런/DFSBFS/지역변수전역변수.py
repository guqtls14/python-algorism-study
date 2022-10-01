def DFS1():
    cnt=3
    print(cnt)

def DFS2():
    global cnt
    if cnt==5:
        # cnt= 하는순간 지역변수화되고 현재 DFS2에는 지역변수가없으므로 에러가남, 이걸해결하려면 global cnt를해서 전역변수를 참조한다고 작성하면됨
        cnt=cnt+1
        print(cnt)


cnt=5
DFS1()
DFS2()
print(cnt)