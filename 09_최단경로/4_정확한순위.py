# 정확한 순위
## 다익스트라(특정 노드에서 출발하여 다른 노드까지 가는)
## 플로이드-워셜(모든 지점에서 다른 모든 지점까지의 최단 경로)
import sys, heapq
sys.stdin = open("09/4.txt", "r")
INF = int(1e9)

student_num, compare = map(int, input().split())
init = [[INF]*student_num for _ in range(student_num)]

# init 초기화
for i in range(student_num):
    for j in range(student_num):
        if i==j:
            init[i][j] = 0

for _ in range(compare):
    lower, higher = map(int, input().split())
    init[lower-1][higher-1] = 1

# 플로이드-워셜
for k in range(student_num):
    for i in range(student_num):
        for j in range(student_num):
            init[i][j] = min(init[i][j], init[i][k]+init[k][j])
# print(*init,sep="\n")

# 성적 순위를 정확히 알 수 있는 학생 총 몇 명인지 -> 끝까지 타고갈 수 있는게 어디까지 인지
ans = 0
for i in range(student_num):
    cnt = 0
    for j in range(student_num):
        if init[i][j] != INF or init[j][i] != INF: # 작은지 큰지 둘 중 하나만 알면
            cnt+=1
    if cnt == student_num:
        ans += 1

print(ans)