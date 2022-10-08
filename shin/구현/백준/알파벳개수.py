a=input()
cnt=[0]*26

for i in a:
    cnt[ord(i)-97]+=1
print(*cnt)

# https://blockdmask.tistory.com/544
# ord: 문자 -> 숫자
# chr: 숫자 -> 문자