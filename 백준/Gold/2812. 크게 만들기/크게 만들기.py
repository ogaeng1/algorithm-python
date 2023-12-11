n, k = map(int, input().split())
num = input()
stack = []

for i in num:
  while stack and stack[-1] < i and k > 0:
    stack.pop()
    k -= 1
  stack.append(i)

print(''.join(stack[:-k] if k > 0 else ''.join(stack)))