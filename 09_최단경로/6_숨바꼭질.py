# 숨바꼭질
from dis import dis
import heapq
import sys
sys.stdin = open("09_최단경로/6.txt", "r")
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
distance = [INF]*(n+1)

# 1번 헛간에서 출발 (0,0)
# 최단거리가 가장 먼 -> 다익스트라

# 다익스트라
start = 1
q = []
heapq.heappush(q,(0,start)) # (비용,경로)
distance[start] = 0
while q:
    dist,now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + 1
        if cost < distance[i]:
            distance[i] = cost
            heapq.heappush(q, (cost,i))

ans_num = 0
ans_dist = max(distance[1:])
ans_dup = 0
for i in range(1,n+1):
    if distance[i]==ans_dist:
        if ans_num==0:
            ans_num = i
        ans_dup += 1

print(ans_num, ans_dist, ans_dup) # 헛간 번호, 헛간까지 거리, 같은 거리를 같은 헛간 개수