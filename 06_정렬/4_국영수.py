# 국영수
## sort함수를 제대로 몰랐네... 
## key에 여러 개 조건 넣을 수 있는 것과, 우선순위 지정 알아서 해주는 것을 몰랐음
import sys
sys.stdin = open("06/4.txt", "r")

num = int(sys.stdin.readline())
student = []
student_kor = []
student_eng = []
student_math = []

# 국어 영어 수학
for _ in range(num):
    name, kor, eng, math = sys.stdin.readline().split()
    student.append((name, int(kor), int(eng), int(math)))

# 1. 국어점수 desc
# 2. 영어점수 asc
# 3. 수학점수 desc
# 4. 이름 사전순
student.sort(key= lambda x : ((-x[1]), x[2], (-x[3]), x[0]))

for s in student:
    print(s[0])
