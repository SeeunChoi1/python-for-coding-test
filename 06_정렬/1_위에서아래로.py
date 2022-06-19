# 위에서 아래로
import sys
sys.stdin = open("06/1.txt", "r")

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)
print(*arr)