# 못생긴 수
import sys
sys.stdin = open("08_DP/9.txt", "r")

# 2,3,5만 소인수로 가지는 수
# n번째 못생긴 수
# 이거 뭔가 피보나치랑 비슷함

n = int(input())
dp = [0]*n
dp[0] = 1

i2, i3, i5 = 0, 0, 0
m2, m3, m5 = 2, 3, 5

for i in range(1,n):
    dp[i] = min(m2, m3, m5)
    if dp[i] == m2:
        i2 += 1
        m2 = dp[i2]*2
    if dp[i] == m3:
        i3 += 1
        m3 = dp[i3]*3
    if dp[i] == m5:
        i5 += 1
        m5 = dp[i5]*5

print(dp[n-1])