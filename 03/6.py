#문자열 뒤집기
import sys
sys.stdin = open("03/6.txt", "r")

given_list = list(map(int, sys.stdin.readline()))
cnt = 0

for i in range(0,len(given_list)-1):
    if given_list[i] != given_list[i+1]:
        cnt += 1

print((cnt+1)//2)

# if cnt%2 == 0:
#     cnt //= 2
# elif cnt == 1 or cnt == 0:
#     cnt
# else:
#     cnt = cnt//2 + 1
# print(cnt)