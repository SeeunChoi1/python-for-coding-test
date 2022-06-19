# 두 배열의 원소 교체
import sys
sys.stdin = open("06/3.txt", "r")

num, change = map(int, input().split())

list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

list_a.sort()
list_b.sort(reverse=True)

# A배열 원소 하나와 B배열 원소 하나를 바꾸기 가능
# A의 모든 원소 합이 최대
for i in range(change):
    if list_a[i] < list_b[i]:
        list_a[i], list_b[i] = list_b[i], list_a[i]
    else: # A의 원소가 B의 원소보다 크거나 같을 때, 반복문 탈출 (이건 생각 못함!)
        break

print(sum(list_a))
