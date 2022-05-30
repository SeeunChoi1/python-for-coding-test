# 고정점 찾기
import sys
sys.stdin = open("07/4.txt", "r")

# 고정점 : 그 값이 인덱스와 동일한 원소
# 오름차순 정렬
# 고정점 출력 (없다면 -1 출력)

num = int(input())
array = list(map(int, input().split()))

# 시간복잡도 O(logN)이면 이진 탐색이지!
start = 0
end = num-1
ans = -1
while start<=end:
    mid = (start+end)//2
    # print(start,end,mid,array[mid])
    if array[mid] == mid:
        # print('break',start,end,mid,array[mid])
        ans = mid
        break
    elif array[mid] < mid:
        start = mid+1
    elif mid < array[mid]:
        end = mid-1
    
print(ans)