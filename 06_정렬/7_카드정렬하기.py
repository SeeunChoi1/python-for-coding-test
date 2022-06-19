# 카드 정렬하기
## 우선순위큐
import sys, heapq
sys.stdin = open("06/7.txt", "r")

n = int(input())
card_size = []
for _ in range(n):
    card_size.append(int(input()))
heapq.heapify(card_size)
ans = 0

# A+B 번의 비교
# 최소한 몇 번의 비교가 필요한지를 구하는 프로그램
# 2개 고르고, 넣고 정렬하고, 젤 작은 2개 고르고
while len(card_size)>1:
    cardA = heapq.heappop(card_size)
    cardB = heapq.heappop(card_size)
    ans += (cardA+cardB)
    heapq.heappush(card_size,cardA+cardB)
    # print(card_size, ans)

print(ans)