# 공유기 설치
import sys
sys.stdin = open("07/5.txt", "r")

# 가장 인접한 두 공유기 사이의 거리 최댓값
## 이진 탐색으로 가장 인접한 두 공유기 사이의 거리를 조절해가며 
## 매 순간 실제로 공유기를 설치하여 div_num보다 많은 개수로 공유기를 설치할 수 있는지 체크
## -> 파라메트릭 서치
house_num, div_num = map(int, input().split())
location = []
for _ in range(house_num):
    location.append(int(input()))
location.sort()

start = location[1]-location[0]
end = location[-1]-location[0]
ans = 0

while (start<=end):        
    mid = (start+end)//2 # 최대거리
    prev_div = location[0]
    cnt = 1
    # 최대거리 유지하면서 공유기 배치
    for i in range(1,house_num):
        if location[i] >= prev_div + mid:
            prev_div = location[i] # 배치했음!
            cnt += 1
    if cnt >= div_num:
        start = mid+1
        ans = mid # 최적의 결과 저장
    else: # 설치 불가해서 거리 줄여야됨
        end = mid-1

print(ans)