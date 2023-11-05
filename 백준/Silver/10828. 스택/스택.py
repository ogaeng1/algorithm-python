import sys

n = int(input())
stack = []

for _ in range(n):
  word = sys.stdin.readline().split()
  if word[0] == "push":
    stack.insert(0, word[1])
  elif word[0] == "pop":
    if stack:
      print(stack[0])
      stack.pop(0)
    else:
      print(-1)
  elif word[0] == "size":
    print(len(stack))
  elif word[0] == "empty":
    if stack:
      print(0)
    else:
      print(1)
  elif word[0] == "top":
    if stack:
      print(stack[0])
    else:
      print(-1)