# 인구이동
import sys
sys.stdin = open("05/9.txt", "r")
from collections import deque

n, left, right = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

# 연합 기준으로 표시
def group(graph):
    visited = [[False]*n for _ in range(n)] #초기화
    group_list = []
    union = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            # 연합 계산 - bfs
            queue = deque()
            queue.append([i,j,union+1])
            visited[i][j] = union+1 # visited에 update

            group_list.append([i,j])
            group_num = 1
            group_sum = graph[i][j]

            while queue: # bfs
                x, y, union = queue.popleft()
                for dx, dy in (1,0), (-1,0), (0,-1), (0,1):
                    nx = x + dx
                    ny = y + dy
                    if nx<0 or nx>=n or ny<0 or ny>=n: # out of range
                        continue
                    if visited[nx][ny]:
                        continue
                    if left <= abs(graph[x][y] - graph[nx][ny]) <= right :
                        queue.append([nx,ny,union])
                        visited[nx][ny] = union # union데리고다니기

                        group_list.append([nx,ny])
                        group_num += 1
                        group_sum += graph[nx][ny]
            print('--------')
            print('union', union, group_list)
            print(visited)

            # bfs 끝 -> 연합 기준 인구수 계산
            new_population = group_sum // group_num
            for elem in group_list:
                visited[elem[0]][elem[1]] = new_population

    return visited, union

ans = 0
while True:
# for _ in range(3):
    new_graph, union = group(graph) # 연합 생성
    print(union)
    if union >= n*n:
        break
    ans += 1   
    graph = new_graph
    print('========')

print('ans >>',ans)