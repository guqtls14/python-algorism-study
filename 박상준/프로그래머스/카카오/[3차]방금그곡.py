"""
 *packageName    : 
 * fileName       : [3차]금방그곡
 * author         : qkrtkdwns3410
 * date           : 2022-08-26
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-26        qkrtkdwns3410       최초 생성
 """


def solution(m, musicinfos):
    answer = '(None)'
    max_length = -1
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    
    for info in musicinfos:
        info_list = info.split(",")
        
        info_list[3] = info_list[3].replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        length = len(info_list[3])
        
        time_diff = int(info_list[1].split(":")[0]) - int(info_list[0].split(":")[0])
        min_diff = int(info_list[1].split(":")[1]) - int(info_list[0].split(":")[1])
        
        total_min = time_diff * 60 + min_diff
        
        if length < total_min:
            i = 0
            while length != total_min:
                info_list[3] = info_list[3] + info_list[3][i]
                length = len(info_list[3])
                i += 1
        elif length > total_min:
            info_list[3] = info_list[3][0:total_min]
        
        print(f"info_list : {info_list[3]}")
        print(f"m : {m}")
        if m in info_list[3]:
            if max_length < len(info_list[3]):
                answer = info_list[2]
                max_length = len(info_list[3])
    
    return answer


print(solution("CC#BCC#BCC#", ["03:00,03:08,FOO,CC#B"]))
print("==========================================")
# print(solution("ABCDEFG", ["13:00,13:15,WORLD,FFFFFFF", "12:00,12:14,HELLO,ABCDEFG"]))
# print("==========================================")
# print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print("==========================================")
# print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
# print("==========================================")
# print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
