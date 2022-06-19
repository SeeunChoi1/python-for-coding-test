# 부품 찾기
import sys
sys.stdin = open("07/1.txt", "r")

all = int(sys.stdin.readline())
all_list = list(map(int, sys.stdin.readline().split()))
want = int(sys.stdin.readline())
want_list = list(map(int, sys.stdin.readline().split()))

all_list.sort()
want_list.sort()

# 부품이 있으면 yes
# 부품이 없으면 no

def counting_sort(all, all_list, want, want_list): # 완전 탐색
    ans = ["no" for _ in range(want)]
    print(all_list, want_list)
    for i in range(want):
        for all in all_list:
            if want_list[i] == all:
                ans[i] = "yes"

    for a in ans:
        print(a, end= ' ')

def binary_search(array, target, start, end): # 이진 탐색
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid # 인덱스 반환
        elif target < array[mid]:
            end = mid -1
        else:
            start = mid+1
    return None

for w in want_list:
    idx = binary_search(all_list, w, 0, all-1)
    if idx != None:
        print("yes", end=" ")
    else:
        print("no", end = " ")