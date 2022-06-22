# 퇴사
import sys
sys.stdin = open("08_DP/7.txt", "r")

day = int(input())
arr = []
dp = [0]*day

for _ in range(day):
    time, pay = map(int, input().split())
    arr.append((time,pay))

# 바텀업
# 뒤에서부터 계산
max_val = 0
for i in range(day-1,-1,-1):
    time = arr[i][0] + i
    if time>day:
        dp[i] = max_val
    else:
        dp[i] = max(arr[i][1]+dp[time], max_val)
        max_val = dp[i]

print(dp)
print(dp[0])