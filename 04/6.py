# 자물쇠와 열쇠

# 시계방향 회전 90, 180, 270
def rotation(key, key_size):
    new_key = [[0 for _ in range(key_size)] for _ in range(key_size)]
    for i in range(key_size):
        for j in range(key_size):
            new_key[j][key_size-i-1] = key[i][j]
    print(*new_key, sep="\n")
    return new_key

    
def solution(key, lock):
    key_size = len(key[0])
    lock_size = len(lock[0])
    count = 0
    for l in lock:
        if l == 0:
            count+=1
    
    # 상하좌우 이동을 위한 확장 lock
    expend_size = 2*key_size+lock_size-2
    expend_lock = [[9]*(expend_size) for _ in range(expend_size)]
    # expend_lock에 원래 lock 채우기
    for i in range(lock_size):
        for j in range(lock_size):
            expend_lock[key_size-1+i][key_size-1+j] = lock[i][j]
    # print("===expended===")
    # print(*expend_lock,sep="\n")
    
    # key 넣는 것 시도
    def try_fit(r,c,expend_lock):
        new_lock = expend_lock
        for i in range(r,r+key_size):
            for j in range(c,c+key_size):
                if new_lock[i][j] == 0:
                    new_lock[i][j] = 1
        return new_lock
    
    # 열렸는가
    def is_fit(new_lock,count):
        tmp_count = 0
        for i in range(lock_size):
            for j in range(lock_size):
                if new_lock[key_size-1+i][key_size-1+j] == 1:
                    tmp_count = True
        if count == tmp_count:
            return True
        else:
            return False
    
    # expend_lock 순회하면서 맞는지 확인
    for i in range(expend_size-key_size+1):
        for j in range(expend_size-key_size+1):
            new_lock = try_fit(i,j,expend_lock) 
            if is_fit(new_lock,count):
                return True
            else:
                print("===circular===", i, j)
                print(*new_lock,sep="\n")
