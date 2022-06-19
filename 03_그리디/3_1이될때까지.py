#1이될때까지
import sys
sys.stdin = open("03/3.txt", "r")

target, div_num = map(int, sys.stdin.readline().split())
ans = 0

#======풀이1======
# while(target>1):
#     if target%div_num == 0:
#         target //= div_num
#     else:
#         target -= 1
#     ans += 1

#======풀이2======
while True:
    tmp = (target//div_num)*div_num #나눌수있는수로 바꾸기
    ans += target-tmp
    target = tmp
    if target<div_num:
        break
    target //= div_num
    ans += 1

#나누지못하는 남은수에 대한 "1빼는 횟수" 계산
ans += target-1

print(ans)