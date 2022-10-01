"""
 *packageName    : 
 * fileName       : 1번
 * author         : ipeac
 * date           : 2022-10-01
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-10-01        ipeac       최초 생성
 """
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def solution(registered_list, new_id):
    # 처음에 n 에 0값이 들어가는지 확인
    flag = False
    st = []
    for i in range(len(new_id)):
        if new_id[i].isnumeric() and int(new_id[i]) in list:
            flag = True
        elif new_id[i].isnumeric() and int(new_id[i]) == 0 and not flag:
            st.append(i)
    if st:
        new_id = new_id[:st[0]] + new_id[st[-1] + 1:]
    
    #  new id 가 해당 문자열 안에 있는지 화깅ㄴ
    if new_id not in registered_list:
        
        return new_id
    
    else:  # 포함되어 있다면
        # new id 를 두 개의 문자열로 분리한다.
        while True:
            if new_id not in registered_list:
                break
            
            number = len(new_id) + 1
            s = ''
            n = ''
            falg = False
            for i in range(len(new_id)):
                if new_id[i].isnumeric() and not falg:
                    number = i
                    falg = True
            
            s = new_id[:number]
            if number != len(new_id) + 1:
                n = new_id[number:]
            
            # 2-2. 문자열 N을 10진수 숫자로 변환한 값을 n이라고 합니다.
            # (단, N이 비어있는 null 문자열이라면, n은 0이 됩니다.)
            if n == "":
                n1 = '10'
            else:  # 빈 문자가 아니라면
                # 2-3. n에 1을 더한 값(n+1)을 문자열로 변환한 값을 N1라고 합니다.
                
                n = int(n)
                n += 1
                n1 = str(n)
                # 2-4. new_id를 S+N1로 변경하고 1.로 돌아갑니다.
            new_id = s + n1
    
    return new_id

print(solution(["card", "ace13", "ace16", "banker", "ace17", "ace14"], "ace15"))
print(solution(["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"], "cow001"))
print(solution(["bird99", "bird98", "bird101", "gotoxy"], "bird98"))
print(solution(["apple1", "orange", "banana3"], "apple"))
