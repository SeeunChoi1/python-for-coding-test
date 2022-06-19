# 기둥과 보

# 기둥 가능 여부
def is_gidung(graph,x,y,n):
    # 바닥 위
    if y==0:
        return True
    # 보의 한쪽 끝
    elif x+1 < n+1 and graph[x+1][y] == 1:
        return True
    elif x-1>0 and graph[x-1][y] == 1:
        return True   
    # 다른 기둥 위
    elif graph[x][y-1] == 0 or graph[x][y+1] == 0:
        return True
    return False

# 보 가능 여부
def is_bo(graph,x,y,n):
    # 한쪽 끝이 기둥
    if y-1>=0 and graph[x][y-1]==0:
        return True
    elif x+1<n+1 and y-1>=0 and graph[x+1][y-1]==0:
        return True
    # 양쪽 끝이 다른 보와 동시에 연결
    elif graph[x+1][y] == 1 and graph[x-1][y] == 1:
        return True
    # 바닥엔 설치할 수 없음
    elif y==0:
        return False
    print('is_bo',x,y)
    return False

# 삭제 가능 여부
def is_delete(graph,n):
    flag = True
    # 순회하면서
    for i in range(0,n+1):
        for j in range(0,n+1):
            if graph[i][j] == 0:
                flag = is_gidung(graph,i,j,n) # 기둥이면 is_gidung에 넣고
                print('gidung here',i,j,flag)
            elif graph[i][j] == 1:
                flag = is_bo(graph,i,j,n)  # 보면 is_bo에 넣어서 확인함
                print('bo here',i,j,flag)
            if not flag:
                print('false here',i,j,flag)
                return flag # 하나라도 False면 False
    return flag

def solution(n, build_frame):
    graph = [[2]*(n+1) for _ in range(n+1)]
    for build in build_frame:
        nx, ny, arch, action = build[0], build[1], build[2], build[3]
        print('build',nx, ny, arch, action)
        if nx<0 or ny<0 or nx>(n+1) or ny>(n+1): # 벽면 벗어남
            print('out of range', nx,ny)
            continue
        if action == 0: #삭제
            # 일단 삭제하고 전체가 맞는지 확인
            graph[nx][ny] = 2
            able = is_delete(graph,n)
            if able:
                print(*graph,sep="\n")
                print('is_delete success',nx,ny)
            else:
                print(*graph,sep="\n")
                print('is_delete fail',nx,ny)
                graph[nx][ny] = arch
        else: #삽입
            able = is_gidung(graph,nx,ny,n) if arch==0 else is_bo(graph,nx,ny,n)
            # answer에 반영하기
            if able:
                graph[nx][ny] = arch
    return graph

n = 5
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

graph = solution(n,build_frame)
print(*graph,sep="\n")

answer = []

for i in range(0,n+1):
    for j in range(0,n+1):
        if graph[i][j] != 2:
            answer.append([i,j,graph[i][j]]) # [구조물x, 구조물y, 기둥/보]
print(answer)

# x, y좌표가 모두 같은 경우 기둥이 보보다 앞에 오면 됩니다.