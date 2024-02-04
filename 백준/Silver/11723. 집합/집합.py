from sys import stdin

m = int(stdin.readline())
data = set()

for _ in range(m):
  cal = list(stdin.readline().split())

  if cal[0] == 'add':
    if int(cal[1]) not in data:
      data.add(int(cal[1]))
  elif cal[0] == 'remove':
      data.discard(int(cal[1]))
  elif cal[0] == 'check':
    if int(cal[1]) in data:
      print(1)
    else:
      print(0)
  elif cal[0] == 'toggle':
    if int(cal[1]) in data:
      data.discard(int(cal[1]))
    else:
      data.add(int(cal[1]))
  elif cal[0] == 'all':
    data = set(range(1, 21))
  elif cal[0] == 'empty':
    data.clear()