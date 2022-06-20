# 1로 만들기
import sys
sys.stdin = open("08_DP/1.txt", "r")

n = int(input())
dp = [0]*30001 # i를 만들기 위한 최소 연산 횟수
ans = 0

for i in range(2,n+1):
    dp[i] = dp[i-1] +1 # 1을 빼는 경우 (일단 뭐하나 값을 세팅해야 min계산을 하니까)
    if i%5==0:
        dp[i] = min(dp[i], dp[i//5]+1)
    elif i%3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    elif i%2==0:
        dp[i] = min(dp[i], dp[i//2]+1)        

print(dp[n])


# 미워
# 너무해
# 슬퍼
# 엉엉