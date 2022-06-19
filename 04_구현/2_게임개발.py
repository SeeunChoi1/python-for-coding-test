#게임 개발
import sys
sys.stdin = open("04/2.txt", "r")

col, row = map(int, sys.stdin.readline().split(' '))
x, y, direction = map(int, sys.stdin.readline().split(' '))
d = [(-1,0),(0,1),(1,0),(0,-1)] #북,동,남,서

# 0 육지 / 1 바다
graph = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(col)]
visited = [ [0]*row for _ in range(col)]

visited[x][y] = 1 #현재 위치 방문 처리

ans = 1
turn_time = 0
while True:
    # 방향전환
    direction -= 1
    if direction == -1:
        direction = 3
    nx = x + d[direction][0]
    ny = y + d[direction][1]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if graph[nx][ny] == 0 and visited[nx][ny] == 0: 
        visited[nx][ny] = 1
        x = nx
        y = ny
        ans += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바디인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4: 
        nx = x - d[direction][0]
        ny = y - d[direction][1]
        # 뒤로 갈 수 있다면 이동하기
        if graph[nx][ny] == 0: 
            x = nx
            y = ny
        # 뒤가 바다로 막힌 경우
        else:
            break
        turn_time = 0

print(ans)