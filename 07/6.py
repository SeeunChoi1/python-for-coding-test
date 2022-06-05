# 가사 검색
import sys

def is_equal(word,query,idx):
    if word[idx] == query[idx]:
        return True
    else:
        return False

def binary_search(word,query,flag,idx):
    # print(flag,idx)
    while (0<= idx <len(word)):
        if is_equal(word,query,idx):
            if flag == 'forward':
                idx += 1
            elif flag == 'backward':
                idx -= 1
        else:
            return False
    return True

def solution(words, queries):
    answer = []

    for query in queries:
        match_num = 0
        # flag: (backward,앞쪽 검사)-fro?? / (forward,뒤쪽 검사) - ???o
        flag = 'forward' if query[0]=='?' else 'backward'
        # idx : ?가 시작되는 위치
        if flag == 'backward':
            idx = query.find('?')-1
        elif flag == 'forward':
            idx = query.rfind('?')+1
        query_len = len(query)
        # tmp = []
        # print('keyword >> ',query,flag,idx)

        for word in words:
            # print('result >>',word, binary_search(word,query,flag,idx))
            if len(word)==query_len and binary_search(word,query,flag,idx):
                match_num += 1
                # tmp.append(word)
        answer.append(match_num)

    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))