from sys import stdin
from collections import deque

N = int(stdin.readline().rstrip()) #컴퓨터 개수
M = int(stdin.readline().rstrip()) #쌍으로 연결된 컴퓨터 개수

lst = [0] * M

virus_lst = deque()
virus_lst.append(1)

for i in range(M):
    start_end = tuple(map(int, stdin.readline().split()))
    lst[i] = start_end

lst.sort()

for i in range(M):
    if(lst[i][0] in virus_lst):
        if(lst[i][1] in virus_lst):
            continue
        else:
            virus_lst.append(lst[i][1])

print(len(virus_lst) - 1)

# 5
# 4
# 1 2
# 2 4
# 3 5
# 4 5 
#반례 해결해야됨
