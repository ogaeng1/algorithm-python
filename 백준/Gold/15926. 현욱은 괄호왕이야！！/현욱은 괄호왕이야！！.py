import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()

stack = []
max_len = 0
pos = -1

for i in range(n):
  if s[i] == '(':
    stack.append(i)
  else:
    if stack:
      stack.pop()
      if stack:
        max_len = max(max_len, i-stack[-1])
      else:
        max_len = max(max_len, i-pos)
    else:
      pos = i

print(max_len)