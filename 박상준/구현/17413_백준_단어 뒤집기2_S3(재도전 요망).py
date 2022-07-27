"""
 *packageName    : 
 * fileName       : 17413_백준_단어 뒤집기2_S3
 * author         : jihye94
 * date           : 2022-07-27
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-27        jihye94       최초 생성
 baekjoon online judge
 noojkeab enilno egduj

 <open>tag<close>
 <open>gat<close>

 <ab cd>ef gh<ij kl>
 <ab cd>fe hg<ij kl>
 """
s = list(input().rstrip())
print("s : %s " % s)
i = 0
while i < len(s):
    if s[i] == "<":
        i += 1
        while s[i] != ">":
            i += 1
        i += 1
    elif s[i].isalnum():
        start = i
        while i < len(s) and s[i].isalnum():
            i += 1
        s[start:i] = reversed(s[start:i])

        print("s : %s " % s)
    else:
        i += 1
print("s : %s " % s)

# https://hongcoding.tistory.com/62
