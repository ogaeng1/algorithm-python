word = input()
boom = input()

stack = []
boom_length = len(boom)

for i in range(len(word)):
  stack.append(word[i])

  if ''.join(stack[-boom_length:]) == boom:
    for _ in range(boom_length):
      stack.pop()

print(''.join(stack) if stack else 'FRULA')