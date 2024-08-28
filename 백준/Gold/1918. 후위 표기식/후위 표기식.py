import sys
input = sys.stdin.readline

stack = []
res = []
priority = { '+': 1, '-': 1, '*': 2, '/': 2 }

s = input().strip()

for i in s:
  if i.isalpha():
    res.append(i)
  elif i == '(':
    stack.append(i)
  elif i == ')':
    while stack and stack[-1] != '(':
      res.append(stack.pop())
    stack.pop()
  else:
    while stack and priority.get(stack[-1], 0) >= priority[i]:
      res.append(stack.pop())
    stack.append(i)
    
while stack:
  res.append(stack.pop())

print(''.join(res))