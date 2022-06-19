#문자열재정렬
import sys
sys.stdin = open("04/4.txt", "r")

stream = sys.stdin.readline()
stream_char = []
stream_int = 0

for i in range(len(stream)):
    if stream[i].isalpha():
        stream_char.append(stream[i])
    else: 
        stream_int += int(stream[i])

#숫자가 하나라도 존재하면 가장 뒤에 삽입
if stream_int != 0:
    print(''.join(sorted(stream_char))+str(stream_int))
else:
    print(''.join(sorted(stream_char)))