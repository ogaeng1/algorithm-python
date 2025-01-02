import sys
from collections import defaultdict

input = sys.stdin.readline
dic = defaultdict(int)

n = int(input())

for _ in range(n):
  num = int(input())
  dic[num] += 1

sorting = sorted(dic.items(), key=lambda x: (-x[1], x[0]))

print(sorting[0][0])
