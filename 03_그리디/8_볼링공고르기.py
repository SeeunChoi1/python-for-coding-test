#볼링공고르기
import sys
sys.stdin = open("03/8.txt", "r")

ball_num, max_weight = map(int, sys.stdin.readline().split(" "))
balls = list(map(int, sys.stdin.readline().split(" ")))
weights = [0 for i in range(max_weight+1)]
ans = 0

#구현
# for i in range(len(balls)-1):
#     for j in range(i,len(balls)):
#         if balls[i] != balls[j]:
#             print(i+1, j+1)
#             ans += 1
# print(ans)

#그리디
##개당 몇개인지 찾고
##경우의수를 만든 뒤 곱한다 -> 여기에서 답안참고
for ball in balls:
    weights[ball] += 1

for i in range(1,max_weight+1):
    ball_num -= weights[i] #남은 갯수 구하기
    ans += weights[i]*ball_num #경우의 수 곱하기
print(ans)
