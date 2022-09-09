"""
 *packageName    : 
 * fileName       : 3613.Java vs C++
 * author         : qkrtkdwns3410
 * date           : 2022-09-09
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-09        qkrtkdwns3410       최초 생성
 """
import sys

n = input()
n_flag = 0
new_n = ''
pass_chk = False
for i in range(len(n)):
    if pass_chk and i != len(n) - 1:
        pass_chk = False
        continue
    if (i == len(n) - 1 and n[i] == '_') or (i == 0 and n[i] == '_') or (i == 0 and n[i].isupper()):
        print("Error!")
        sys.exit(0)
    
    if n[i] == '_':
        if n_flag != 0 and n_flag != 1:
            print("Error!")
            exit(0)
        
        n_flag = 1
        if n[i + 1] == '_' or n[i + 1].isupper():
            print("Error!")
            exit(0)
        
        new_n += n[i + 1].upper()
        pass_chk = True
    elif n[i].isupper():
        if n_flag != 0 and n_flag != 2:
            print("Error!")
            exit(0)
        
        n_flag = 2
        new_n += '_' + n[i].lower()
    else:
        new_n += n[i]

print(new_n)
