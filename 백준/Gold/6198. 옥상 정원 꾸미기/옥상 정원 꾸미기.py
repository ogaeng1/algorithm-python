import sys

N = int(sys.stdin.readline())
building = [int(sys.stdin.readline()) for _ in range(N)]

stack = []
cnt = 0

for i in building:
  while stack and stack[-1] <= i:
    stack.pop()
  stack.append(i)
 
  cnt += len(stack) -1

print(cnt)