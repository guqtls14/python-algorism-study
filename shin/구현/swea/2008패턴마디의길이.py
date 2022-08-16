for i in range(int(input())):
    s=input()
    for j in range(1,10):
        if s[:j]==s[j:j*2]:
            print(f'#{i+1} {j}')
            break