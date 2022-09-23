"""
 *packageName    : 
 * fileName       : 2661.좋은수열
 * author         : ipeac
 * date           : 2022-09-18
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-09-18        ipeac       최초 생성
 """

n = 7  # 입력


def is_good_arr(arr):
    arr_len = len(arr)
    # 절반 만큼 확인
    for part_len in range(1, arr_len // 2 + 1):  # 비교할 부분수열의 길이
        for part_start in range(part_len, arr_len - part_len + 1):
            # 같은 부분의 수열을 발견한다면
            if arr[part_start - part_len:part_start] == arr[part_start:part_start + part_len]:
                return False
    else:  # 모든 부분의 수열이  다르면
        return True


def dfs(arr, depth):
    if depth == n:
        print("".join(list(map(str, arr))))
        exit(0)
    arr.append(1)
    for i in range(1, 4):
        arr.pop()
        arr.append(i)
        if is_good_arr(arr):
            if not dfs(arr, depth + 1):
                continue
    else:  # 1~3 사이에 좋은 수열이 없는 경우
        arr.pop()
        return False


dfs([1], 1)  # 백트래킹
