# 팀 결성
## 서로소 집합 알고리즘
import sys
sys.stdin = open("10_기타_그래프_이론/1.txt", "r")

# 특정 원소가 속한 집합 찾기
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+1)

for i in range(n+1):
    parent[i] = i

for i in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0: # union
        union_parent(parent,a,b)
    elif oper == 1: # find
        if find_parent(parent, a) == find_parent(parent, b): # 같은 팀 여부 확인
            print("YES")
        else:
            print("NO")