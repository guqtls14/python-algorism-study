t = int(input())

for tc in range(1, t + 1) :
    hour, minute, next_hour, next_minute = map(int, input().split())
    result_hour = hour + next_hour

    result_minute = minute + next_minute

    if result_minute > 59 :
        result_hour += 1
        result_minute -= 60

    if result_hour > 12 :
        result_hour -= 12

    print('#%d %d %d' % (tc, result_hour, result_minute))