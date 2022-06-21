# 퇴사
import sys
sys.stdin = open("08_DP/7.txt", "r")

day = int(input())
arr = []
dp = [0]*day

for _ in range(day):
    time, pay = map(int, input().split())
    arr.append((time,pay))
print(arr)

# 바텀업
left_time = 0
pick_pay = 0
for i in range(day):
    # 진행되던 것 없음 or 하던거 끝남
    if left_time == 0: 
        if pick_pay == 0: # 진행되던 것 없음
            left_time = arr[i][0]-1
            pick_pay = arr[i][1]
            if left_time == 0: # 골랐는데 바로 끝남
                dp[i] += pick_pay
                left_time, pick_pay = 0, 0
        else: # 하던거 끝남
            dp[i] += pick_pay
            left_time, pick_pay = 0, 0
    # 진행되던 것 있음
    else: 
        if (i+1)+arr[i][0]<=day and i-1>=0:
            dp[i] = max(dp[i-left_time]+arr[i][1], dp[i-1])
        left_time -= 1
print(dp)
