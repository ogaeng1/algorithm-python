while True:
  text = input()
  stack = []
  if text == '.':
    break
  
  for i in text:
    if i == '(' or i == '[':
      stack.append(i)
    elif i == ')':
      if len(stack) != 0 and stack[-1] == '(':
        stack.pop()
      else:
        stack.append(i)
        break
    elif i == ']':
      if len(stack) != 0 and stack[-1] == '[':
        stack.pop()
      else:
        stack.append(i)
        break
  print('yes' if len(stack) == 0 else 'no')