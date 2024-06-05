import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
num = deque(enumerate(map(int, input().split())))
ballon = []

while num:
  idx, paper_num = num.popleft()
  ballon.append(idx+1)
  
  if paper_num > 0:
    num.rotate(-(paper_num-1))
  else:
    num.rotate(-paper_num)

print(*ballon)