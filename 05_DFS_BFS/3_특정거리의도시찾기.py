# 특정 거리의 도시 찾기
## 최단 거리가 k인 것
## visited를 0으로 초기화했더니 83%에서 틀렸습니다. 놓친 코너케이스가 있는 듯
import sys
sys.stdin = open("05/3.txt", "r")
from collections import deque

node, edge, k, start = map(int, sys.stdin.readline().split())
graph= [[] for _ in range(node+1)]
for _ in range(edge):
    start_city, end_city = map(int, sys.stdin.readline().split())
    graph[start_city].append(end_city)

visited = [-1]*(node+1) # 거리 초기화
visited[start] = 0 # 출발지는 0
isNone = True

#bfs
queue = deque()
queue.append(start)
while queue:
    now = queue.popleft()
    for next_node in graph[now]:
        if visited[next_node] == -1:
            queue.append(next_node)
            visited[next_node] = visited[now] + 1

for i in range(1,len(visited)):
    if visited[i] == k:
        print(i)
        isNone = False
if isNone:
    print(-1)