# 금광
from stringprep import in_table_c11_c12
import sys
sys.stdin = open("08_DP/5.txt", "r")

case_num = int(input())
for _ in range(case_num):
    n, m = map(int, input().split())
    input_arr = list(map(int, input().split()))
    arr = [[-1 for _ in range(m)] for _ in range(n)]
    dp = [[-1 for _ in range(m)] for _ in range(n)] # max라 -1로 초기화

    r = 0
    c = 0
    for i in range(len(input_arr)):
        arr[r][c] = input_arr[i]
        c += 1
        if c%4 == 0:
            r += 1
            c = 0

    for i in range(n):
        dp[i][0] = arr[i][0]

    for k in range(m):
        a,b,c = 0,0,0
        for i in range(n):
            for j in range(1,m):
                a = j-1 if j-1>0 else 0
                b = i+1 if i+1<n else i
                c = i-1 if i-1>0 else 0
                dp[i][j] = arr[i][j] + max(dp[i][a], dp[b][a], dp[c][a])

    # print(*dp,sep="\n")
    ans = 0
    for i in range(n):
        ans = max(ans,dp[i][m-1])
    print(ans)