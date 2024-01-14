import sys

n = int(sys.stdin.readline())
meet = []

for _ in range(n):
  start, end = map(int, sys.stdin.readline().split())
  meet.append((start, end))

meet.sort(key=lambda x: (x[1], x[0]))

end_time = 0
res = 0

for i in meet:
  if end_time <= i[0]:
    end_time = i[1]
    res += 1

print(res)