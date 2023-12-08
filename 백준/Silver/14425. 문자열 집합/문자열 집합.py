n, m = map(int, input().split())

s = set([input() for _ in range(n)])
cnt = 0

for _ in range(m):
  word = input()
  if word in s:
    cnt += 1

print(cnt)