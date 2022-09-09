# for t in range(1, T+1) :
#     N = int(input())
#     a = 0; b = 0; c = 0; d = 0; e = 0
#     while(N != 1) :
#         if N % 2 == 0 :
#             a += 1
#             N = N/2
#         elif N % 3 == 0 :
#             b += 1
#             N = N/3
#         elif N % 5 == 0 :
#             c += 1
#             N = N/5
#         elif N % 7 == 0 :
#             d += 1
#             N = N/7
#         elif N % 11 == 0 :
#             e += 1
#             N = N/11

#     print("#{0} {1} {2} {3} {4} {5}".format(t, a, b, c, d, e))


T = int(input())
for tc in range(1, T+1):
    # 입력으로 받은 N을
    N = int(input())
    # 소인수 리스트를 만들어서
    num = [2, 3, 5, 7, 11]
    # 나눠진 횟수를 담기위한 빈 리스트 생성
    count = [0, 0, 0, 0, 0]
    # 리스트 num을 돌면서(range로 한 이유는 같은 인덱스에 count리스트에도 횟수를 추가해주기 위해서)
    for n in range(len(num)):
        # 무한루프를 주고
        while True:
            # 만약 N이 num의 n번째 숫자로 나눈 나머지가 0이라면
            if N % num[n] == 0:
                # N은 그 숫자로 나눈 몫으로 바꾸고
                N = N//num[n]
                # count리스트의 같은 인덱스에 값을 +1해줌
                count[n] += 1
            # 나눈 나머지가 0이 아니라면 멈추고 num의 다음 인덱스로 넘어감.
            else:
                break
    # 리스트컴프리핸션을 이용한 출력
    # print('#{}'.format(tc),' '.join([str(_) for _ in count]))
    # map함수는 str을 count의 모든항목에 적용
    print('#{}'.format(tc), ' '.join(map(str, count)))

    # 특정에 해당하는 원소의 갯수를 세는 문제