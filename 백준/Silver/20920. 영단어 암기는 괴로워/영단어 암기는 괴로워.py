import sys

n, m = map(int, sys.stdin.readline().split())

dic = dict()

for _ in range(n):
  word = sys.stdin.readline().strip()

  if len(word) < m:
    continue
  else:
    if word in dic:
      dic[word] += 1
    else:
      dic[word] = 1

words = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for i in words:
  print(i[0])