PPAP = input()
stack = []

for i in PPAP:
  stack.append(i)

  if len(stack) >= 4 and stack[-4:] == ['P', 'P', 'A', 'P']:
    stack.pop()
    stack.pop()
    stack.pop()

print('PPAP' if len(stack) == 1 and stack[0] == 'P' else 'NP')