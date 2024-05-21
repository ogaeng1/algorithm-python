import sys
input = sys.stdin.readline

N = list(input().strip())
M = int(input().strip())
stack = []

for _ in range(M):
  c = input().strip()

  if c[0] == 'L' and N:
    stack.append(N.pop())
  elif c[0] == 'D' and stack:
    N.append(stack.pop())
  elif c[0] == 'B' and N:
    N.pop()
  elif c[0] == 'P':
    N.append(c[-1])

print("".join(N + stack[::-1]))