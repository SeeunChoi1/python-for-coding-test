
# 문자열 압축 (프로그래머스 https://programmers.co.kr/learn/courses/30/lessons/60057)
def solution(s):
    answer = []
    if len(s) == 1:
        return 1
    for i in range(1,(len(s)//2)+1):
        reslut = ''
        cnt = 1
        test = s[:i]
        for j in range(i,len(s),i):
            if test == s[j:i+j]:
                cnt += 1
            else:
                if cnt != 1:
                    reslut = reslut+str(cnt)+test
                else:
                    reslut = reslut+test
                test = s[j:j+i]
                cnt = 1
        if cnt != 1:
            reslut = reslut+str(cnt)+test
        else:
            reslut = reslut+test
        answer.append(len(reslut))
    return min(answer)