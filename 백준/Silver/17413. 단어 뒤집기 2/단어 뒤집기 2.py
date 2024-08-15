import sys
input = sys.stdin.readline

input_str = input().strip()
stack = []
res = ''
bracket = False

for s in input_str:
  if s == '<':
    while stack:
      res += stack.pop()
    bracket = True
    res += s
  elif s == '>':
    bracket = False
    res += s
  elif bracket:
    res += s
  elif s == ' ':
    while stack:
      res += stack.pop()
    res += s
  else:
    stack.append(s)

while stack:
  res += stack.pop()

print(res)