# 편집 거리
import sys
sys.stdin = open("08_DP/10.txt", "r")

# 문자열A -> 문자열B를 위한 연산 수
# 삽입 / 삭제 / 교체
# 이걸 2차원 배열쓸 생각을 어떻게 하냐고..ㅂㄷㅂㄷ

strA = input()
strB = input()
lenA = len(strA)
lenB = len(strB)

dp = [[0]*(lenB+1) for _ in range(lenA+1)]
for i in range(1,lenA+1):
    dp[i][0] = i
for j in range(1,lenB+1):
    dp[0][j] = j

for i in range(1,lenA+1):
    for j in range(1,lenB+1):
        # 같음
        if strA[i-1] == strB[j-1]:
            dp[i][j] = dp[i-1][j-1]
        # 다름
        else:
            dp[i][j] = min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j])+1 # 생성,변경,삭제

print(*dp,sep='\n')
print(dp[lenA][lenB])