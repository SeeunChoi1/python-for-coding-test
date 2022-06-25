# 정수 삼각형
import sys
sys.stdin = open("08_DP/6.txt", "r")

# 이제까지 선택된 수의 합이 최대가 되는 경로
# 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택

tri_size = int(input())
dp = []
for _ in range(tri_size):
    dp.append(list(map(int,input().split())))

for i in range(1,tri_size):
    for j in range(i+1):
        if j==0: # 왼쪽 끝
            up_left = 0
        else:
            up_left = dp[i-1][j-1]
        if j==i: # 오른쪽 끝
            up = 0
        else:
            up = dp[i-1][j]
        dp[i][j] = dp[i][j] + max(up_left, up)

print(dp)
print(max(dp[tri_size-1]))