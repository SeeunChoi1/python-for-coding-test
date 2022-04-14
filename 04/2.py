#게임 개발
import sys
sys.stdin = open("04/2.txt", "r")

col, row = map(int, sys.stdin.readline().split(' '))
col_now, row_now, direction = map(int, sys.stdin.readline().split(' '))
d = [(0,-1),(1,0),(0,-1),(-1,0)] #북,동,남,서

# 0 육지 / 1 바다
graph = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(col)]
print(graph)

# 왼쪽부터 갈 곳을 정함
# 가보지않은 칸이 있다면, 왼쪽으로 회전 후 전진
# 가보지 않은 칸이 없다면, 왼쪽으로 회전만
# 네방향 다 가봤거나 바다인 경우, 방향을 유지한채 한칸 뒤로감
# 뒤가 바다라서 움직일 수 없으면 멈춤