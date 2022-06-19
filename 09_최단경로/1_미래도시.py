# 미래 도시
## 양방향 그래프!
import sys
sys.stdin = open("09/1-2.txt", "r")
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# k번 회사를 거쳐 x번 회사로 가는 최소 이동 시간
# 도달할 수 없다면 -1 출력
comp_num, edge_num = map(int, input().split())
graph = [[INF]*comp_num for _ in range(comp_num)]

# 자기자신 0으로 초기화
for r in range(comp_num):
    for c in range(comp_num):
        if r==c:
            graph[r][c] = 0

# 연결된 라인은 +1
for _ in range(edge_num):
    a,b = map(int, input().split())
    if graph[a-1][b-1] == INF:
        graph[a-1][b-1] = 1
        graph[b-1][a-1] = 1
    else:
        graph[a-1][b-1] += 1
        graph[b-1][a-1] += 1

x_comp, k_comp = map(int, input().split())

# 플로이드-워샬
for k in range(comp_num):
    for a in range(comp_num):
        for b in range(comp_num):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# print(*graph,sep='\n')
ans =  graph[0][k_comp-1] + graph[k_comp-1][x_comp-1]
if ans >= INF:
    ans = -1
print(ans)