# 자물쇠와 열쇠
## 도저히 풀다가 GG치고 검색해봤는데 그냥 뇌절와서 완성 못한 것같기도 함

# 시계방향 회전 90, 180, 270
def rotation(key, key_size):
    new_key = [[0 for _ in range(key_size)] for _ in range(key_size)]
    for i in range(key_size):
        for j in range(key_size):
            new_key[j][key_size-i-1] = key[i][j]
    return new_key

# 열렸는가
def is_fit(startX, startY, lock, key, expend_size, start, end):
    expend_lock = [[0]*(expend_size) for _ in range(expend_size)]
    
    # expend_lock에 lock 채우기
    for i in range(start,end):
        for j in range(start,end):
            expend_lock[i][j] += lock[i-start][j-start]
    
    # expend_lock에 key 채우기
    for i in range(len(key)):
        for j in range(len(key)):
            expend_lock[startX+i][startY+j] += key[i][j]
            
    # 다 채웠으니 확인하기
    for i in range(start,end):
        for j in range(start,end):
            if expend_lock[i][j] != 1:
                return False
    return True
    
def solution(key, lock):
    key_size = len(key[0])
    lock_size = len(lock[0])
    
    # expend_lock에서 lock의 원래 위치 (start,start) ~ (end,end)
    start = len(key)-1
    end = start + len(lock)
    # 상하좌우 이동을 위한 확장 lock의 size
    expend_size = 2*key_size+lock_size-2 
    
    # expend_lock 순회하면서 맞는지 확인
    for _ in range(0,4): # rotate key
        for i in range(end):
            for j in range(end):
                if is_fit(i,j,lock,key,expend_size,start,end):
                    return True
        key = rotation(key, key_size)
    return False
                
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key,lock))