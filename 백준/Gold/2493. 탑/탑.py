N = int(input())
top_height = list(map(int, input().split()))

res = [0] * N
stack = []

for i in range(N):
  while stack:
    if top_height[stack[-1][0]] < top_height[i]:
      stack.pop()
    else:
      res[i] = stack[-1][0] + 1
      break

  stack.append([i, top_height[i]])

print(*res)