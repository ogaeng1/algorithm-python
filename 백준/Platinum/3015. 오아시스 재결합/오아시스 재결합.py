import sys
input = sys.stdin.readline

stack = []
N = int(input())
height = [int(input()) for _ in range(N)]

res = 0

for i in range(N):
  while stack and stack[-1][0] < height[i]:
    res += stack.pop()[1]

  if not stack:
    stack.append([height[i], 1])
  else:
    if stack[-1][0] == height[i]:
      cur = stack[-1][1]
      res += cur
      stack[-1][1] = cur+1
      if len(stack) > 1:
        res += 1
    else:
      stack.append([height[i], 1])
      res += 1

print(res)