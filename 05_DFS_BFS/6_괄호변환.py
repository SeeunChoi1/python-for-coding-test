# 괄호변환
## 시키는 대로 풀기
## 균형잡힌 괄호 문자열 분리가 생각보다 어려웠따...
import sys
sys.stdin = open("05/6.txt", "r")

p = input()
# 올바른 괄호 문자열 판별
def isRightString(p): 
    stack = []
    for char in p:
        if char == '(':
            stack.append(char)
        elif char == ')' and stack:
            stack.pop()
    if not stack: # stack이 비어야 True
        return True
    else:
        return False
    
# 균형잡힌 괄호 문자열로 분리        
def toBalanced(p): 
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        elif p[i] == ')':
            cnt -= 1
        if cnt == 0: # 균형이 맞으면 바로 return
            return i
    
def solution(p):
    if not p:
        return ""
    if isRightString(p):
        return p
    
    idx = toBalanced(p)
    u,v = p[:idx+1], p[idx+1:]
    if isRightString(u):
        return u+solution(v)
    else:
        empty_string = "("+solution(v)+")"
        new_u = u[1:-1]
        tmp_u = ''
        for tmp in new_u:
            if tmp == '(':
                tmp_u += ')'
            elif tmp == ')':
                tmp_u += '('
        return empty_string+tmp_u