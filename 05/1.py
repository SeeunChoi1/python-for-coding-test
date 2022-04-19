# 음료수 얼려 먹기
import sys
sys.stdin = open("05/1.txt", "r")

n,m = map(int, input().split())
graph = [list(map(int,input())) for _ in range(n)]
direction = [(-1,0),(0,1),(1,0),(0,-1)] # 이동방향
answer = 0
answer2 = 0

def dfs(c, r):
    # 연결된 구멍은 다 1로 만들어줌
    for i in range(4):
        dc = c + direction[i][0]
        dr = r + direction[i][1]
        if dc<=-1 or dc>=n or dr<=-1 or dr>=m: # out of range
            continue
        if graph[dc][dr] == 1:
            continue
        graph[c][r] = 1
        dfs(dc, dr)
    
def dfs2(c,r):
    if c<=-1 or c>=n or r<=-1 or r>=m:
        return False
    if graph[c][r] == 0:
        graph[c][r] = 1
        dfs2(c-1,r)
        dfs2(c,r-1)
        dfs2(c+1,r)
        dfs2(c,r+1)
        # for i in range(4):
        #     dc = c+direction[i][0]
        #     dr = r+direction[i][1]
        #     dfs2(dc,dr)
        return True
    return False

# 이어진 0 갯수
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            continue
        else:
            print(">>",i,j)
            answer += 1
            dfs(i,j)

for i in range(n):
    for j in range(m):
        if dfs2(i,j):
            print('--',i,j)
            answer2 += 1

print(answer)
print(answer2)