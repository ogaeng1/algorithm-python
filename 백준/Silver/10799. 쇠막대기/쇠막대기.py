import sys
input = sys.stdin.readline

stick = input().strip()
stack = []
res = 0

for i in range(len(stick)):
  if stick[i] == '(':
    stack.append('(')
  else:
    stack.pop()
    if stick[i-1] == '(':
      res += len(stack)
    else:
      res += 1

print(res)