# 가사 검색_ans
## bisect 라이브러리 안쓰고 하고싶었는데ㅠ.ㅠ
from bisect import bisect_left, bisect_right
import sys

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array,left_value,right_value):
    left_index = bisect_left(array,left_value)
    right_index = bisect_right(array,right_value)
    return right_index - left_index

def solution(words, queries):
    answer = []

    # 길이별로 분리한 hashmap
    array = [[] for _ in range(100001)]
    reversed_array = [[] for _ in range(100001)]
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for i in range(100001):
        array[i].sort()
        reversed_array[i].sort()

    for query in queries:
        if query[0] != '?':
            ans = count_by_range(array[len(query)],query.replace('?','a'),query.replace('?','z'))
        else:
            ans = count_by_range(reversed_array[len(query)],query[::-1].replace('?','a'),query[::-1].replace('?','z'))
        answer.append(ans)
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))