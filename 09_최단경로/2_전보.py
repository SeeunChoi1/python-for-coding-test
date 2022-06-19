# 전보
## 단방향 그래프
## 한 도시에서 다른 도시까지의 최단 거리 문제
import heapq
import sys
sys.stdin = open("09/2.txt", "r")
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

city_num, tunnle_num, start_city = map(int, input().split())
graph = [[] for _ in range(city_num+1)]
distance = [INF] * (city_num+1)

for _ in range(tunnle_num):
    start,end,weight = map(int, input().split())
    graph[start].append((end,weight))

q = []
heapq.heappush(q,(0,start_city)) # weight,node
distance[start_city] = 0
while q:
    # 가장 최단거리가 짧은 노드
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    # 인접 node 확인
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]: # 새 cost가 원래 있던 것 보다 작으면
            distance[i[0]] = cost
            heapq.heappush(q, (cost,i[0]))
# print(distance)

cnt = 0 # C에서 보낸 메시지를 받는 도시의 수
max_time = 0 # 메시지를 받는데 걸리는 시간
for d in distance:
    if d != INF:
        cnt+=1
        max_time = max(max_time,d)

print(cnt-1, max_time)