import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
res = []

for _ in range(n):
  war_info = list(map(int, input().split()))
  Ti = war_info[0]
  soldier = war_info[1:]

  soldier_cnt = Counter(soldier)
  conquer = Ti // 2

  conquer_army = ''
  
  for army_num, cnt in soldier_cnt.items():
    if cnt > conquer:
      conquer_army = army_num
      break

  if conquer_army:
    print(conquer_army)
  else:
    print('SYJKGW')