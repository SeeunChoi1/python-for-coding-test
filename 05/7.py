# 연산자 끼워 넣기
## 백트래킹
## 경우의 수
## 그래프가 아닌 dfs
import sys
sys.stdin = open("05/7.txt", "r")

n = int(input())
number = list(map(int,input().split()))
operator = list(map(int,input().split())) # +, -, *, /
return_max, return_min = float('-inf'), float('inf')

def dfs(i, value, operator):
    global return_max, return_min
    if i == n: # 숫자 계산 완료
        return_max = max(return_max, value)
        return_min = min(return_min, value)
    else:
        if operator[0] > 0: # 덧셈
            operator[0] -= 1
            dfs(i+1,value+number[i],operator)
            operator[0] += 1
        if operator[1] > 0: # 뺄셈
            operator[1] -= 1
            dfs(i+1,value-number[i],operator)
            operator[1] += 1
        if operator[2] > 0: # 곱셈
            operator[2] -= 1
            dfs(i+1,value*number[i],operator)
            operator[2] += 1
        if operator[3] > 0: # 나눗셈
            operator[3] -= 1
            dfs(i+1,int(value/number[i]),operator)
            operator[3] += 1


dfs(1,number[0],operator)
print(return_max)
print(return_min)