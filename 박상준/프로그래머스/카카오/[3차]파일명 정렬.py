"""
 *packageName    : 
 * fileName       : [3차]파일명 정렬
 * author         : ipeac
 * date           : 2022-08-27
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-08-27        ipeac       최초 생성
 """


def solution(files):
    new_files = []
    answer = []
    
    for i, value in enumerate(files):
        inner_list = ["", "", ""]
        index_of = 0
        for index, k, in enumerate(value):
            
            if index_of == 0 and k.isdigit():
                index_of = 1
            if index_of == 1 and not k.isdigit():
                index_of = 2
            inner_list[index_of] += k
            pass
        new_files.append(inner_list)
    
    new_files.sort(key=lambda x: [x[0].lower(), int(x[1]) * 100])
    for value in new_files:
        insert_value = ""
        for item in value:
            insert_value += item
        answer.append(insert_value)
    return answer


print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
