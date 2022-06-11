# 화성 탐사
## 다익스트라(특정 노드에서 출발하여 다른 노드까지 가는)
## bfs??
## 플로이드-워샬
import sys, heapq
sys.stdin = open("09/5.txt", "r")
INF = int(1e9)
dxy = [(1,0),(0,1),(-1,0),(0,-1)]

# 화성 탐사 기계 이동 최적 경로 계산
# 상하좌우 인접 1칸 이동 가능
# 좌표 하나 - 노드 하나

case_num = int(input())
for _ in range(case_num):
    size = int(input())
    graph = [list(map(int, input().split())) for _ in range(size)]
    distance = [[INF]*size for _ in range(size)]

    # 다익스트라
    q = []
    heapq.heappush(q,(graph[0][0],(0,0))) # weight, node
    distance[0][0] = graph[0][0]
    while q:
        dist, now = heapq.heappop(q)
        if distance[now[0]][now[1]] < dist:
            continue
        for d in dxy:
            nx = now[0]+d[0]
            ny = now[1]+d[1]
            if nx<0 or ny<0 or nx>=size or ny>=size: # out of range
                continue
            cost = dist + graph[nx][ny]
            if cost<distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q,(cost,(nx,ny)))
    print(distance[size-1][size-1])