t = int(input())

for i in range(1, t + 1) :
    n = input()
    value = int(n)
    data = [0] * 10
    while True :
        for j in range(len(n)) :
            data[int(n[j])] += 1
        if not data.count(0) :
            print('#%d %d' % (i, int(n)))
            break

        n = str(value+int(n))

# 문자열조작
# 리스트 인덱싱

