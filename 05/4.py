# 연구소
import sys
from unittest import result
sys.stdin = open("05/4.txt", "r")

col, row = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(col)]
test = [[0]*row for _ in range(col)] #울타리 세울 때 쓸 list
dir = [(1,0),(-1,0),(0,-1),(0,1)] #상하좌우
ans = 0

# 0-빈칸 / 1-벽 / 2-바이러스
# dfs로 바이러스를 전파시킨다
def dfs(x,y):
    test[x][y] = 2
    for i in range(4):
        nx = x + dir[i][0]
        ny = y + dir[i][1]
        if nx<0 or nx>=col or ny<0 or ny>=row : # out of range
            continue
        if test[nx][ny] == 1 : # 벽이라 넘어감
            continue
        if test[nx][ny] == 0 : # not visited
            dfs(nx,ny)

# 남은 0의 갯수를 센다
def calculate():
    cnt = 0
    for col in test:
        for elem in col:
            if elem == 0:
                cnt += 1
    return cnt

def fence(count):
    global ans, result
    # 울타리 3개 완료
    if count == 3: 
        
        # if graph[1][0] and graph[0][1] and graph[3][5]:
        #     print(">>>>>start>>>>>" , count)
        #     print(*graph, sep='\n')
        # 2행 1열, 1행 2열, 4행 6열
        for i in range(col):
            for j in range(row):
                test[i][j] = graph[i][j]
        # 전파 시작
        for i in range(col):
            for j in range(row):
                if test[i][j] == 2:
                    dfs(i,j)
        result = max(result, calculate())
        # if graph[1][0] and graph[0][1] and graph[3][5]:
        #     print(">>>>>temp>>>>>", result)
        #     print(*test, sep='\n')
        return
    # 벽을 세운다
    for i in range(col):
        for j in range(row):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                fence(count)
                graph[i][j] = 0
                count -= 1
result = -1
fence(0)
print(result)