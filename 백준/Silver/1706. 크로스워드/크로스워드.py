import sys
input = sys.stdin.readline

R, C = map(int, input().strip().split())

puzzle = [input().strip() for _ in range(R)]
res = []

for i in puzzle:
  row_word = i.split('#')
  for j in row_word:
    if len(j) > 1:
      res.append(j)

for i in range(C):
  col_word = ''.join([puzzle[j][i] for j in range(R)])
  for j in col_word.split('#'):
    if len(j) > 1:
      res.append(j)

res.sort()
print(res[0])