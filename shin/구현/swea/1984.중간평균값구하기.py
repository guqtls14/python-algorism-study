n=int(input())

for _ in range(1,n+1):
    a=list(map(int, input().split()))

    a.sort()

    a.remove(max(a))
    a.remove(min(a))

    print('#{} {}'.format(_,round(sum(a)/len(a),1)))