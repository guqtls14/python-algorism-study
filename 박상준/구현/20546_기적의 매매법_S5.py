"""
 *packageName    : 
 * fileName       : 20546_기적의 매매법_S5
 * author         : ipeac
 * date           : 2022-07-29
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2022-07-29        ipeac       최초 생성
 """
# 준현이 성민이 현금
money = int(input())
machine_duck_price = list(map(int, input().split()))

jun_money = money
jun_stock_count = 0
sung_money = money
sung_stock_count = 0

# 14일 동안 거래
for i in range(len(machine_duck_price)):
    if jun_money >= machine_duck_price[i]:
        # 준현 - 무한 매수
        stock_count_plus = jun_money // machine_duck_price[i]
        jun_money -= machine_duck_price[i] * jun_money // machine_duck_price[i]
        jun_stock_count += stock_count_plus
    
    # 성민 - 프로그램 매수
    if sung_money < machine_duck_price[i]:
        continue
    else:
        # 연속거래 고려
        if i >= 3:
            if machine_duck_price[i - 3] > machine_duck_price[i - 2] > machine_duck_price[i - 1] > machine_duck_price[i]:
                stock_count_plus = sung_money // machine_duck_price[i]
                sung_money -= machine_duck_price[i] * sung_money // machine_duck_price[i]
                sung_stock_count += stock_count_plus
            elif machine_duck_price[i - 3] < machine_duck_price[i - 2] < machine_duck_price[i - 1] < machine_duck_price[i]:
                # 주식 전량 판매
                sung_money += machine_duck_price[i] * sung_stock_count
                sung_stock_count = 0

jun_final = jun_money + (machine_duck_price[len(machine_duck_price) - 1] * jun_stock_count)
sung_final = sung_money + (machine_duck_price[len(machine_duck_price) - 1] * sung_stock_count)

if jun_final > sung_final:
    print("BNP")
elif jun_final < sung_final:
    print("TIMING")
else:
    print("SAMESAME")
