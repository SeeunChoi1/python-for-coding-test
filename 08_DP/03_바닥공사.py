# 바닥 공사
import sys
sys.stdin = open("08_DP/3.txt", "r")

n = int(input())
dp = [0]*1001

dp[0] = 0
dp[1] = 1
dp[2] = 3
for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]*2 # 모든 경우의 수

print(dp[n])