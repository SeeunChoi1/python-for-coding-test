# 실패율
## 정렬
## TODO : failure 하나로 다 합치기
import sys


def solution(N,stages):
    answer = []

    # 실패율 = 도달했으나 클리어 못함 / 도달한 플레이어 수
    # [클리어 못함, 도달한 플레이어 수]
    not_clear = [0 for _ in range(N+2)]
    reached = [0 for _ in range(N+2)]
    failure = [[0,0] for _ in range(N+2)]
    stages.sort()
    print(stages)

    for stage in stages:
        not_clear[stage] += 1 # 클리어 못한 플레이어 수 증가

    reached[len(not_clear)-1] = not_clear[len(not_clear)-1]
    for i in reversed(range(1,len(not_clear)-1)):
        reached[i] = not_clear[i] + reached[i+1]

    print(not_clear)
    print(reached)

    for i in range(1,N+2):
        failure[i][0] = i
        if reached[i] == 0: # dividen by 0
            failure[i][1] = 0
        else:
            failure[i][1] = not_clear[i] / reached[i]
    print(failure)

    failure.sort(key=lambda x : x[1], reverse=True)
    print(failure)

    for fail in failure:
        if fail[0] == N+1 or fail[0] == 0: # padding 삭제
            continue
        answer.append(fail[0])

    return answer


N = 4
stages = [4,4,4,4,4]	
print(solution(N,stages))