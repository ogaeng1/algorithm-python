import sys
input = sys.stdin.readline

n = int(input())
stack = [tuple(map(int, input().split())) for _ in range(n)]
stack.sort()
max_height, idx = 0, 0

for i in range(n):
  if max_height < stack[i][1]:
    max_height = stack[i][1]
    idx = i

left, right = 0, 0
res = 0

for i in range(idx+1):
  if stack[i][1] > left:
    left = stack[i][1]
  if i < idx:
    res += left * (stack[i+1][0]-stack[i][0])
  else:
    res += left * (stack[idx][0]-stack[i][0])

for i in range(n-1, idx, -1):
  if stack[i][1] > right:
    right = stack[i][1]
  res += right * (stack[i][0]-stack[i-1][0])

print(res + max_height)