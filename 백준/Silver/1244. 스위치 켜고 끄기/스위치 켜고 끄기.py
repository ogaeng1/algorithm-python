import sys

N = int(sys.stdin.readline())
switch_status = [False] + list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

for _ in range(M):
    gender, num = map(int, sys.stdin.readline().split())
    if gender == 1 :
        for i in range(1, N//num+1):
            if switch_status[i*num] == 0 :
                switch_status[i*num] = 1
            else     :
                switch_status[i*num] = 0
    if gender == 2 :
        if switch_status[num] == 0:
            switch_status[num] = 1
        else :
            switch_status[num] = 0
        l_switch, r_switch = num-1, num+1
        while l_switch > 0 and r_switch <= N and switch_status[l_switch] == switch_status[r_switch]:
            if switch_status[l_switch] == 0:
                switch_status[l_switch], switch_status[r_switch] = 1,1
            else :
                switch_status[l_switch], switch_status[r_switch] = 0,0
            l_switch = l_switch - 1
            r_switch = r_switch + 1

for k in range(1,N+1):
    print(switch_status[k], end=" ")
    if k % 20 == 0:
        print()
