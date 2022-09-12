"""
 *packageName    : 
 * fileName       : 행렬의 곱셈
 * author         : qkrtkdwns3410
 * date           : 2022-09-12
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-12        qkrtkdwns3410       최초 생성
 """

def solution(arr1, arr2):
    answer = []
    # 0 1 2
    for i in range(len(arr1)):
        tmp_arr = []
        # 0 1 2
        for j in range(len(arr1[0])):
            tmp = 0
            for k in range(len(arr2[0])):
                print("==========================================")
                print(f"arr1 : {arr1[i][k]}")
                print(f"arr1 : {arr2[k][j]}")
                tmp += arr1[i][k] * arr2[k][j]
            print(f"tmp : {tmp}")
            tmp_arr.append(tmp)
        answer.append(list(tmp_arr))
    return answer

# solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]])
solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]])
