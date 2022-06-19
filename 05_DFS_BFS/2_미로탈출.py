# 미로 탈출
## 최단 거리는 주로 bfs로 많이 푼다
## 최단 거리 구할 때 다른 공통변수 만들 생각하지 말고 누적해서 더할 생각을 해보자
## nc랑 nr구할 때 계속 leftpop된 v에서 가져오는게 아니라 c,v에서 더하는 실수를 했다
## 변수명을 예쁘면서 직관적으로 정할 수 있도록 하기!
import sys
sys.stdin = open("05/2.txt", "r")

from collections import deque

col, row = map(int, input().split())
graph = [list(map(int,input())) for _ in range(col)]
dir = [(1,0),(0,1),(-1,0),(0,-1)]
result = []

# 0 - 못지나감
# 1 - 지나감
def bfs(c,r):
    queue = deque()
    queue.append([c,r])
    while queue:
        v = queue.popleft()
        # result.append(v)
        for i in range(4):            
            nc = v[0]+dir[i][0]
            nr = v[1]+dir[i][1]
            if nc<0 or nc>=col or nr<0 or nr>=row: # out of range
                continue
            if graph[nc][nr] == 0: # 못지나감
                continue
            # 지나감
            # 해당 노드를 처음 방문하면 최단거리 기록
            if graph[nc][nr] == 1:
                graph[nc][nr] = graph[v[0]][v[1]]+1
                queue.append([nc,nr])
    # 마지막 노드가 항상 최솟값인가?
    return graph[col-1][row-1]

print(bfs(0,0))
for row in graph:
    print(row)
print(result)