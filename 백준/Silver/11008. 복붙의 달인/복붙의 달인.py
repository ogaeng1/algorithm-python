t = int(input())

for _ in range(t):
  s, p = input().split()

  s = s.replace(p, '*')
  print(len(s))