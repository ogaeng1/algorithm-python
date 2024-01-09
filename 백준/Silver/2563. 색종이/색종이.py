paper = [[0] * 100 for _ in range(100)]

n = int(input())

for _ in range(n):
  x, y = map(int, input().split())

  for i in range(x, x+10):
    index_x = i
    for j in range(y, y+10):
      index_y = j

      if paper[index_x][index_y] == 0:
        paper[index_x][index_y] = 1

cnt = 0

for i in range(100):
  cnt += sum(paper[i])

print(cnt)