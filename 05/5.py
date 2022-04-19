# 경쟁적 전염
## dfs 여러 번 호출하는 방식으로 풀면200(i) * 200(j) * 10,000(s) =  400,000,000 (40억인가요.. ?) 이기 때문에 시간초과
## 반드시 bfs(큐)로 풀어야하는 문제
## deque는 정렬이 안되기 때문에 정렬된 list를 deque로 변환
import sys
sys.stdin = open("05/5.txt", "r")
from collections import deque

# 매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식
# S초가 지난 후에 (X,Y)에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성
size, max_virus = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(size)]
second, end_col, end_row = map(int, input().split())
direction = [(-1,0),(0,1),(1,0),(0,-1)] #상하좌우

virus = []
for i in range(size):
    for j in range(size):
        if graph[i][j] != 0:
            virus.append((graph[i][j], i, j, 1))
virus.sort()
queue = deque(virus)

while queue:
    (now_virus, x, y, trial) = queue.popleft()
    if trial == second+1:
        break
    for dir in direction:
        nx = x+dir[0]
        ny = y+dir[1]
        if nx<0 or nx>=size or ny<0 or ny>=size : # out of range
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = now_virus
            queue.append((now_virus, nx, ny, trial+1))

print(graph[end_col-1][end_row-1])