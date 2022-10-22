# from collections import Counter

# n=int(input())

# for i in range(1,n+1):
#     a=int(input())
#     li=list(map(int,input().split()))
#     answer = Counter(li).most_common(1)
#     print('#{} {}'.format(a,answer[0][0]))

T = int(input())
for i in range(T):
    test_number = int(input())
    scores = list(map(int, input().split()))
    mode = 0  # 1

    # 2
    count_dic = {}
    for i in scores:
        if i in count_dic:
            count_dic[i] += 1
        else:
            count_dic[i] = 1
    print(count_dic)
    # 3
    max_count = 0
    for key, value in count_dic.items():
        if max_count < value:  # 4
            max_count = value
            mode = key
        elif max_count == value:  # 5
            if mode < key:
                mode = key
    # 6
    print('#{} {}'.format(test_number, mode))

    # https://zetawiki.com/wiki/SWEA_1204_(S/W_%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0_%EA%B8%B0%EB%B3%B8)_1%EC%9D%BC%EC%B0%A8_-_%EC%B5%9C%EB%B9%88%EC%88%98_%EA%B5%AC%ED%95%98%EA%B8%B0