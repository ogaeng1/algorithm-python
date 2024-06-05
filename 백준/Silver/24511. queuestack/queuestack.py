import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

dq = deque()

for i in range(N):
  if A[i] == 0:
    dq.appendleft(B[i])

for i in range(M):
  dq.append(C[i])

print(*list(dq)[:M])