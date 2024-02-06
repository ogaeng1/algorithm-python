from sys import stdin

n, m = map(int, stdin.readline().split())

dic = dict()

for _ in range(n):
  site = input().split()
  dic[site[0]] = site[1]

for _ in range(m):
  password = input()
  print(dic[password])