def DFS(v):
    if v==n+1:
        for i in range(1,n+1):
            if ch[i] == 1:
                print(i,end=' ')
        print()
    else:
        # 만일 v==n+1아니면 사용한다는것이므로 1로체크
        ch[v]=1
        # 그다음 수 체크
        DFS(v+1)
        # v=n+1이 만족되면 다시 되돌아가서 숫자를 비교해야함
        ch[v]=0
        DFS(v+1)

n=int(input())
ch=[0]*(n+1)
DFS(1)