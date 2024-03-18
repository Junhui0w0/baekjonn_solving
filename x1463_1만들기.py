from sys import stdin

N = int(stdin.readline().rstrip())

count = 0
while(True):
    if(N == 1):
        break
    else:
        if(N == 10):
            count = count + 3
            break
        elif(N % 3 == 0): #3으로 나눠떨어지면
            N = N // 3
            count += 1
        elif(N % 2 == 0):
            N = N // 2
            count += 1
        else:
            N = N - 1
            count += 1
print(count)