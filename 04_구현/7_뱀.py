# 뱀
import sys
sys.stdin = open("04/7.txt", "r")

board_num = int(input())
board = [[(0,0) for _ in range(board_num)] for _ in range(board_num)] #(뱀/사과/빈여부, 이동방향) - 꼬리 삭제시 활용

apple_num = int(input())
for _ in range(apple_num):
    x,y = map(int, input().split())
    board[x-1][y-1] = (1,0)

# L 왼쪽 -1
# D 오른쪽 +1
d = [(0,1),(1,0),(0,-1),(-1,0)] #동,남,서,북
change_list = [] #(몇초후, 방향)
d_change = int(input())
for _ in range(d_change):
    num, dir = input().split()
    change_list.append([int(num), -1 if dir == "L" else 1])

def turn(d_now, d_change):
    d_now += d_change
    if d_now<0:
        d_now = 3
    if d_now>3:
        d_now = 0
    return d_now

head_r,head_c,d_now = 0,0,0
tail_r,tail_c = 0,0
board[head_r][head_c] = (-1, d_now) # 뱀몸이 있는 자리
time = 0
while True:
    # print("------", time, "------")
    # print(head_r,head_c)
    # print(*board, sep="\n")
    # 방향 찾기
    if change_list and change_list[0][0] == time:
        v = change_list.pop(0)
        d_now = turn(d_now, v[1])
        board[head_r][head_c] = (-1,d_now)

    # 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.   
    head_r += d[d_now][0]
    head_c += d[d_now][1]

    # 벽 또는 자기자신의 몸과 부딪히면 게임이 끝
    if head_r<0 or head_r>=board_num or head_c<0 or head_c>=board_num: # out of range
        break
    if board[head_r][head_c][0] == -1:
        break

    # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
    if board[head_r][head_c][0] == 1:
        board[head_r][head_c] = (-1,d_now)
    # 만약 이동한 칸에 사과가 없다면,
    else:
        board[head_r][head_c] = (-1,d_now) # 일단 머리는 이동
        d_info = board[tail_r][tail_c]

        # 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다
        board[tail_r][tail_c] = (0,d_info[1])
        # 꼬리 정보 update
        tail_r += d[d_info[1]][0]
        tail_c += d[d_info[1]][1]
        
    time += 1

print(time+1)