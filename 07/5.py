# 공유기 설치
import sys
sys.stdin = open("07/5.txt", "r")

# 가장 인접한 두 공유기 사이의 거리를 가능한 크게
# 가장 인접한 두 공유기 사이의 최대 거리 출력
house_num, div_num = map(int, input().split())
location = []
install = []
for _ in range(house_num):
    location.append(int(input()))
location.sort()

start = 0
end = house_num-1
install.append(location[start])
install.append(location[end])
div_num -= 2

def binary_search(start,end):
    global div_num
    while start<=end and div_num>0:        
        mid = (start+end)//2
        install.append(location[mid])
        div_num -= 1
        if div_num % 2 ==0:
            binary_search(start,mid)
        else:
            binary_search(mid,end)

binary_search(start,end)
install.sort()

ans = install[-1]-install[0]
for i in reversed(range(1,len(install))):
    ans = min(ans, install[i]-install[i-1])

print(ans)