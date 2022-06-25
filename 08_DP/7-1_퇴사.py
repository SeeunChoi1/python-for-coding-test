# 퇴사
# dfs
import sys
sys.stdin = open("08_DP/7.txt", "r")

day = int(input())
arr = []
for _ in range(day):
    time, pay = map(int, input().split())
    arr.append((time,pay))
max_pay = 0

def backtracking(idx,acc_pay):
    global max_pay
    if idx > day:
        return
    if idx == day:
        if max_pay < acc_pay:
            max_pay = acc_pay
        return
    backtracking(idx+1,acc_pay) # 상담을 안하고 다음 건으로 바로 넘어감
    if idx + arr[idx][0] <= day: # 상담 가능
        backtracking(idx+arr[idx][0], acc_pay+arr[idx][1])

backtracking(0,0)
print(max_pay)