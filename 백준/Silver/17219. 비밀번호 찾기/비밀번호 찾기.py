from sys import stdin

n, m = map(int, stdin.readline().split())

dic = dict()

for _ in range(n):
  site, password = stdin.readline().split()
  dic[site] = password

for _ in range(m):
  password = stdin.readline().strip()
  print(dic[password])