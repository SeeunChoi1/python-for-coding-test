# 외벽점검2
import itertools
def solution(n, weak, dist):

    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)

    answer = len(dist) + 1

    # 출발 점 정하기
    for start in range(length):
        # dist 의 최대값이 8, 모든 경우의 수를 다 뽑아도 8!
        for friends in list(itertools.permutations(dist, len(dist))):
            count = 1
            # 친구가 끝까지 갈 수 있는 점 구하기
            end = weak[start] + friends[count-1]
            # 갯수를 보겠다 는 것
            for idx in range(start, start+length):
                # 더 이상 점검할 수 없는 경우
                if weak[idx] > end:
                    # 다른 친구를 투입
                    count += 1
                    # 더이상 남은 친구가 없다면
                    if count > len(dist):
                        break
                    end = weak[idx] + friends[count-1]
            answer = min(answer, count)

    return answer if answer < len(dist) + 1 else -1

n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
solution(n, weak, dist)