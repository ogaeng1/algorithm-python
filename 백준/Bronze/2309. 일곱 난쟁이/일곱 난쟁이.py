from itertools import combinations

dwarf = []
for _ in range(9):
  n = dwarf.append(int(input()))
  
dwarf.sort()

res = combinations(dwarf, 7)

for i in res:
  if sum(i) == 100:
    for j in i:
      print(j)
    break