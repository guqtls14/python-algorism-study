


t = int(input())
for i in range(1, t + 1):
    print('#{}'.format(i))
    n = int(input())
    di={}
    for _ in range(n):
        ci,ki=input().split()
        
        di[ci]=int(ki)
    length=0
    for a in di.keys():
        for number in range(di[a]):
            print(a,end='')
            length+=1
            if length % 10 ==0:
                print()
    print()
# 참고 https://velog.io/@shon4bw/SWEA-1946-%EA%B0%84%EB%8B%A8%ED%95%9C-%EC%95%95%EC%B6%95-%ED%92%80%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC 

