# 플로이드
## 모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값
## -> 플로이드-워샬
import sys
sys.stdin = open("09/3.txt", "r")
INF = int(1e9)

city_num = int(input())
bus_num = int(input())
graph = [[INF]*city_num for _ in range(city_num)]

# graph 초기화
for _ in range(bus_num):
    start,end,weight = map(int,input().split())
    # 시작과 도착 도시를 연결하는 노선은 하나가 아닐 수 있음
    if weight < graph[start-1][end-1]: 
        graph[start-1][end-1] = weight

for i in range(city_num):
    for j in range(city_num):
        if i==j:
            graph[i][j] = 0

# 플로이드-워샬 알고리즘
for k in range(city_num):
    for i in range(city_num):
        for j in range(city_num):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
# print(*graph,sep='\n') 

for i in range(city_num):
    for j in range(city_num):
        if graph[i][j] == INF:
            print(0, end= " ")
        else:
            print(graph[i][j], end = " ")
    print()