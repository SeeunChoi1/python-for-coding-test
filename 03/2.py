#숫자카드게임
import sys
sys.stdin = open("03/2.txt", "r")

col, row = map(int, sys.stdin.readline().split())
ans = []

for _ in range(col):
    graph = list(map(int, sys.stdin.readline().split()))
    ans.append(min(graph))
print(max(ans))