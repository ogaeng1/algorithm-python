import sys
input = sys.stdin.readline

N = int(input())
list = [int(input()) for _ in range(N)]
list.sort(reverse=True)

for i in list:
  print(i)