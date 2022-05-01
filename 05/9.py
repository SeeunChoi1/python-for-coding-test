# 인구이동
import sys
sys.stdin = open("05/9.txt", "r")
from collections import deque

n, left, right = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited =  [[False]*n for _ in range(n)]
dx = [1,-1,0,0] #상하좌우
dy = [0,0,-1,1]
group_list = []

# 연합 기준으로 표시
def group(x,y):
    queue = deque([[x,y]])
    # visited[x][y] = True
    while queue:
        v = queue.popleft()
        # v랑 연결된 애들 loop
        # nx,ny = 옆나라
        # v[0],v[1] = 지금나라
        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n: # out of range
                continue
            population = abs(graph[v[0]][v[1]] - graph[nx][ny])
            print(graph[v[0]][v[1]],graph[nx][ny])
            if not visited[nx][ny] and (left <= population and population <= right):
                queue.append([nx,ny])
                visited[nx][ny] = 1
                group_list.append([nx,ny])

# 인구수 계산 후 graph에 반영
def calcPopulation(group_list):
    group_num = len(group_list)
    group_sum = 0
    new_population = 0
    # 인구수 계산
    for group_elem in group_list:
        group_sum += graph[group_elem[0]][group_elem[1]]
    new_population = group_sum // group_num
    # graph 반영
    for group_elem in group_list:
        graph[group_elem[0]][group_elem[1]] = new_population

ans = 0
while True:
# for _ in range(3):
    visited = [[False]*n for _ in range(n)] #초기화
    for i in range(n):
        for j in range(n):
            group(i,j)
    print(visited)
    flag = False # 변경할만한 연합이 나오는지
    for row in visited:
        for elem in row:
            if elem:
                flag = True
    if not flag:
        print('break')
        break
    calcPopulation(group_list)  
    print(graph)
    ans += 1   
    print('========')

print(graph)
print(ans)