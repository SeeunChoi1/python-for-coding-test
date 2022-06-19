#왕실의 나이트
import sys
sys.stdin = open("04/1.txt", "r")

start_col, start_row = sys.stdin.readline()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1
ans = 0

dx = [2,2,-2,-2,1,-1,1,-1]
dy = [1,-1,1,-1,-2,-2,2,2]
col = ['a','b','c','d','e','f','g','h']
start = [col.index(start_col),int(start_row)-1]

for i in range(8):
    nx = start[0]+dx[i]
    ny = start[1]+dy[i]
    if 0<=nx<=7 and 0<=ny<=7:
        ans += 1
print(ans)