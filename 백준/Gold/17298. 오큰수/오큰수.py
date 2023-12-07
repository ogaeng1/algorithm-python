import sys

n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

nge = [-1] * n
stack = []

for i in range(n):
  while stack and num_list[stack[-1]] < num_list[i]:
    nge[stack.pop()] = num_list[i]
  stack.append(i)

print(*nge)