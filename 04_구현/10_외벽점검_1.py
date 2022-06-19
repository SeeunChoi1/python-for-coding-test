# 외벽점검1
# 점검 시간 : 1시간
# 최소한의 친구들을 투입 해 외벽 점검 함
# 정북 방향 -> 시계 방향

# 취약 지점을 점검하기 위해 보내야 하는 친구 수의 최소값
# 취약 지점을 전부 점검할 수 없는 경우에는 -1을 return 해주세요.
# 4.5m -> 0.5의 관리 방안

import collections

'''
n = 5 [0, 1, 2, 3, 4]
pick = 3 

level 1 0                        1       2

level 2 1         2      3       2       3

level 3 2   3   4  3  4  4      3   4   4
'''


def combi(idx, n, pick, tmp):
    # global start_points, visited
    # print("level =", len(tmp), tmp)

    if len(tmp) == pick:
        start_points.append(tmp[:])
        return
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = 1
            combi(i+1, n, pick, tmp+[i])
            visited[i] = 0

def permu(idx, n, pick, tmp):
    # global picked_friends

    if len(tmp) == pick:
        picked_friends.append(tmp[:])
        return
    for i in range(idx, n):
        permu(i+1, n, pick, tmp+[i])


def check_wall(weak, start, friends, dist, n):
    # 지도 -> 외벽이 있어
    # 외벽 다 돌았는 지 확인
    # return True, False
    my_map = [0 for _ in range(n)]
    for w in weak:
        my_map[w] = 1


    for num in friends:
        distance = dist[num]
        end = (start[num] + distance) % n
        for now in (start[num], end+1):
            my_map[now] -= 1

    # 확인
    for w in weak:
        if my_map[w] != 0:
            return False
    return True




def solution(n, weak, dist):
    global visited, start_points, picked_friends
    answer = -1
    # 3. 누구 투입 할지 permutation 으로 뽑아 줌

    num_friends = len(dist)
    # 2. 몇 명 투입 할지 1~dist의 길이만큼
    for pick in range(1, num_friends + 1):
        # pick : 내가 몇 명 뽑을 것 인지
        # 1. 출발 지점 정하기 combination ( 0.5 -> 이하/이상의 의미로 이해함. )
        # n C pick
        start_points = []
        visited = [0 for _ in range(n)]
        combi(0, n, pick, [])

        picked_friends = []
        permu(0, n, pick, [])

        # 외벽 점검




    return answer

n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
solution(n, weak, dist)