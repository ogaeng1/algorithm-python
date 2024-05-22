from collections import deque
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().rstrip()[1:-1].split(',')

    if arr[0] != '':
        arr = deque(map(int, arr))
    else:
        arr = deque()

    error = False
    r_count = 0

    for cmd in p:
        if cmd == 'R':
            r_count += 1
        elif cmd == 'D':
            if len(arr) == 0:
                error = True
                print('error')
                break
            else:
                if r_count % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()

    if not error:
        if r_count % 2 == 1:
            arr.reverse()
        print('[' + ','.join(list(map(str, arr))) + ']')