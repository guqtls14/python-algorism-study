
knight = input()

col=ord(knight[0])-96
row=int(knight[1])


steps=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

# 8방향 위치확인
result=0
for step in steps:
    next_row = row + step[0]
    next_column = col + step[1]

# 탈출안되는조건
    if next_row >=1 and next_row <=8 and next_column >=1 and next_column <=8:
        result+=1
print(result)