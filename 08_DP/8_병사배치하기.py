# 병사 배치하기
## LIS
import sys
sys.stdin = open("08_DP/8.txt", "r")

n = int(input())
arr = list(map(int, input().split()))
dp = [1]*n

for i in range(n-1,-1,-1):
    for j in range(i-1,-1,-1):
        if arr[j]>arr[i]:
            dp[j] = max(dp[j],dp[i]+1)
   
print(n-max(dp))