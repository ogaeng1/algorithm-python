n = int(input())
text = list(input())

for _ in range(n-1):
  word = list(input())
  for j in range(len(word)):
    if text[j] != word[j]:
      text[j] = '?'

print(''.join(text))