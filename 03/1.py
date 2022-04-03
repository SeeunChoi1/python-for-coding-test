#큰수의법칙
import sys
sys.stdin = open("03/1.txt", "r")

arr_len, add_num, max_repeat = map(int,sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
ans = 0
cnt = 0

arr.sort(reverse=True)
#======풀이1======
# for _ in range(add_num):
#     if cnt<max_repeat:
#         cnt += 1
#         ans += arr[0]
#     else:
#         cnt = 0
#         ans += arr[1]

#======풀이2======
#가장 큰수가 더해지는 횟수 계산
count = int(add_num/(max_repeat+1))*max_repeat
count += add_num % (max_repeat+1)

ans += count*arr[0]
ans += (add_num-count)*arr[2]

print(ans)