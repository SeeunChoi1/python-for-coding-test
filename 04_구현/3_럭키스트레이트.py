#럭키 스트레이트
import sys
sys.stdin = open("04/3.txt", "r")

#n을 반으로 나누어 반반 자릿수의 합이 동일
score = list(map(int, sys.stdin.readline()))
break_point = len(score)//2
score1 = 0
score2 = 0

for i in range(break_point):
    score1 += score[i]
    score2 += score[break_point+i]

if (score1 == score2):
    print("LUCKY")
else:
    print("READY")