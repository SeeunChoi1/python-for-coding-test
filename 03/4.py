#모험가 길드
import sys
sys.stdin = open("03/4.txt", "r")

num = sys.stdin.readline()
fear_arr = list(map(int, sys.stdin.readline().split()))
ans = 0
cnt = 0

#모든 여행가를 넣을 필요는 없음
#여행떠나는 그룹의 최대값
##그룹 갯수를 최대로 만드려면 공포도가 낮은 애들부터
fear_arr.sort()

for fear in fear_arr:
    cnt += 1
    if cnt>=fear:
        ans += 1
        cnt = 0
print(ans)