# 떡볶이 떡 만들기
import sys
sys.stdin = open("07/2.txt", "r")

num, want = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
cut_point = 0

array.sort()

# 이진 탐색
start = 0
end = max(array)
while start<=end:
    result = 0
    mid = (start+end)//2
    for a in array: # 자른다
        if a>=mid:
            result += a-mid
        else:
            continue
    # 여기 break 안걸어주면 loop돔
    if result == want:
        cut_point = mid
        break
    # 잘린 애들이 want보다 작으면 왼쪽 (더 잘려야함)
    elif result < want:
        end = mid - 1
    # 잘린 애들이 크면 오른쪽으로 이동한다 (덜 잘려야함)
    else:
        cut_point = mid 
        start = mid +1

print(cut_point)