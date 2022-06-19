# 정렬된 배열에서 특정 수의 개수 구하기
## 이진탐색 라이브러리 사용해서 해결 ver
from bisect import bisect_left, bisect_right
import sys
sys.stdin = open("07/3.txt", "r")

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array,left_value,right_value):
    left_index = bisect_left(array,left_value)
    right_index = bisect_right(array,right_value)
    return right_index - left_index

num, target = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

count = count_by_range(array,target,target)

if count == 0:
    print(-1)
else:
    print(count)