# 정렬된 배열에서 특정 수의 개수 구하기
## 수열 오름차순
## x가 등장하는 횟수 계산
## 시간 복잡도 O(logN)
import sys
sys.stdin = open("07/3.txt", "r")

num, target = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
answer = 0

# 처음 위치를 찾는 메소드
def first(array,target,start,end):
    if start>end:
        return None
    mid = (start+end)//2
    # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid==0 or target>array[mid-1]) and array[mid] == target:
        return mid
    # 중간점의 값 보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
    elif array[mid] >= target:
        return first(array,target,start,mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return first(array,target,mid+1,end)

# 마지막 위치를 찾는 메소드
def last(array,target,start,end):
    if start>end:
        return None
    mid = (start+end)//2
    # 해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
    if (mid==num-1 or target<array[mid+1]) and array[mid] == target:
        return mid
    # 중간점의 값 보다 찾고자 하는 값이 작은 경우 왼쪽 확인(왜 여기서 >= 이면 안되는거지...)
    elif array[mid] > target:
        return last(array,target,start,mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return last(array,target,mid+1,end)

# 정렬된 수열에서 값이 x인 원소의 개수를 세는 메소드
def count(array,target):
    first_idx = first(array,target,0,num-1)
    last_idx = last(array,target,0,num-1)
    
    if first_idx==None or last_idx==None:
        return -1
    else:
        return last_idx-first_idx+1

print(count(array,target))