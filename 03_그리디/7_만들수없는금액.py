#만들수없는금액
import sys
sys.stdin = open("03/7.txt", "r")

coin_num = int(sys.stdin.readline())
coins = list(map(int, sys.stdin.readline().split(" ")))
coins.sort()

#답안 참고
target = 1 #만들수없는 금액 후보

for coin in coins:
    if target<coin: 
        break #다음 동전 단위로 target을 만들 수 없음
    target += coin

print(target)