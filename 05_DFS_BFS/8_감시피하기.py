# 감시 피하기
import sys
sys.stdin = open("05/8.txt", "r")

n = int(input())
graph = [ list(input().split()) for _ in range(n) ]
blank = []
teacher = []
obstacle = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'X':
            blank.append([i,j])
        if graph[i][j] == 'T':
            teacher.append([i,j])
dx = [0,0,-1,1] #상하좌우
dy = [1,-1,0,0]

def setObstacle(idx,tmp): #dfs combination
    global obstacle
    if len(tmp) == 3:
        obstacle.append(tmp[:])
        return
    for i in range(idx,len(blank)):
        setObstacle(i+1,tmp+[blank[i]])

def findStudent(x,y):
    for i in range(4):
        nx = x
        ny = y
        while True:
            nx = nx+dx[i]
            ny = ny+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n: # out of range
                break
            if graph[nx][ny] == 'S':
                # print('학생 찾았다', nx,ny)
                return True
            elif graph[nx][ny] == 'O':
                break
    return False

def teacherFind():
    for t in teacher:
        if findStudent(t[0],t[1]):
            return True
    return False

setObstacle(0,[])

ans = False
for obs in obstacle:
    for x,y in obs:
        graph[x][y] = 'O'
    if not teacherFind():
        ans = True
        break
    for x,y in obs:
        graph[x][y] = 'X'

if ans:
    print("YES")
else:
    print("NO")