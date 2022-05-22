# 안테나
## 그리디, 정렬
import sys
sys.stdin = open("06/5.txt", "r")

num = int(input())
homes = list(map(int, input().split()))
homes.sort()

# 안테나로부터 모든 집까지의 거리의 총 합이 최소
# 안테나는 집이 위치한 곳에만 설치 가능

print(homes[(num-1)//2])