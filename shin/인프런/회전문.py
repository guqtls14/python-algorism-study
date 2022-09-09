n=int(input())

# for  _ in range(n):
#     word = input().upper()
    
#     for i in range(len(word)//2):
#         if word[i] != word[len(word)-i-1]:
#             print('{} NO'.format(_+1))
#             break
#         else:
#             print('{} YES'.format(_+1))
#             break

# for i in range(n):
#     s=input().upper()
#     for j in range(len(s)//2):
#         if s[j] != s[-1-j]:
#             print('{} NO'.format(i+1))
#             break
#         else:
#             print('{} YES'.format(i+1))
#             break

for i in range(n):
    s=input().upper()
    if s == s[::-1]:
        print('{} YES'.format(i+1))
    else:
        print('{} NO'.format(i+1))