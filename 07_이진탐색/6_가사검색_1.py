# 가사 검색
import sys

def solution(words, queries):
    answer = []

    # 길이별로 분리한 hashmap
    map = [[] for _ in range(100001)]
    reversed_map = [[] for _ in range(100001)]
    for word in words:
        map[len(word)].append(word)
        reversed_map[len(word)].append(word[::-1]) # reverse

    for i in range(100001):
        map[i].sort()
        reversed_map[i].sort()

    for query in queries:
        target_idx = map[len(query)]
        match_num = 0
        # flag: (backward,앞쪽 검사)-fro?? / (forward,뒤쪽 검사)-???o
        flag = 'forward' if query[0]=='?' else 'backward'
        # idx : ?가 시작되는 위치
        if flag == 'backward':
            idx = query.find('?')
        elif flag == 'forward':
            idx = query.rfind('?')+1
        elif query[0]=='?' and query[-1]=='?':
            answer.append(len(target_idx))
            continue
        # tmp = []
        # print('keyword >> ',query,flag,idx)

        for target in target_idx:
            if flag == 'forward' and target[idx:]==query[idx:]:
                match_num += 1
            elif flag == 'backward' and target[:idx]==query[:idx]:
                match_num += 1
        answer.append(match_num)
        # print(tmp)

    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))