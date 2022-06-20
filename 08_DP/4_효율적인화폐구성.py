# 효율적인 화폐 구성
import sys
sys.stdin = open("08_DP/4-2.txt", "r")

n_kind,m_amount = map(int, input().split())
coins = []
for _ in range(n_kind):
    coins.append(int(input()))

dp = [10001]*(m_amount+1)
dp[0] = 0
# 순서만 다른 것은 같은 것으로 분류
# 최소한으로 사용해서 가치의 합이 M원
# 불가능하면 -1

# 바텀업
# for i in range(m_amount):
#     for coin in coins:
#         if dp[i-coin] != 10001:
#             dp[i] = min(dp[i-coin]+1,dp[i])

for coin in coins:
    for i in range(coin,m_amount+1):
        if dp[i-coin] != 10001:
            dp[i] = min(dp[i-coin]+1, dp[i])

print(dp[m_amount] if dp[m_amount]!=10001 else -1)