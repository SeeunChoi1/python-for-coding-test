# 개미 전사
import sys
sys.stdin = open("08_DP/2.txt", "r")

# 최소 한 칸 이상 떨어진 창고 약탈
# 얻을 수 있는 식량의 최대값
room_num = int(input())
food = list(map(int, input().split()))
dp = [0]*100 # i개의 창고를 약탈했을 때

# 바텀업
# 그냥 홀수번, 짝수번 한 다음에 둘중 큰거 하면 되는거 아닌가...
# 뭔가 반례가 있을 것같은데...
dp[0] = food[0]
dp[1] = max(food[0], food[1])
for i in range(2,room_num):
    dp[i] = max(dp[i-1], dp[i-2]+food[i])

print(dp[room_num-1])