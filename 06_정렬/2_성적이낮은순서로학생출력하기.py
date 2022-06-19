# 성적이 낮은 순서로 학생 출력하기
import sys
sys.stdin = open("06/2.txt", "r")

n = int(input())
arr = []

for _ in range(n):
    name, score = input().split()
    arr.append([name,int(score)])

arr.sort(key = lambda x : x[1] )

for d in arr:
    print(d[0], end=" ")