#곱하기 혹은 더하기
import sys
sys.stdin = open("03/5.txt", "r")

given_list = list(map(int, sys.stdin.readline()))
ans = 0

for given in given_list:
    #0이나 1이 나오면 더하기
    if given==1 or given == 0 or ans == 0:
        ans += given
    #아니면 곱하기
    else:
        ans *= given
print(ans)