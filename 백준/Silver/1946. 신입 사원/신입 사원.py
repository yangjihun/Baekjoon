import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())  # 신입사원 수
    key = 100001  # 최고값
    result = 0  # 최종 인원수
    li = []  # 신입사원 리스트
    for i in range(N):
        li.append(list(map(int,input().split())))
    li.sort(key = lambda x:x[0])
    
    for junior in li:
        if key > junior[1]:
            key = junior[1]
            result+=1
    print(result)