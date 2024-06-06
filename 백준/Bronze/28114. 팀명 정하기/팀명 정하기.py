import sys
input = sys.stdin.readline

info = []

for _ in range(3):
  solve, year, name = input().split()
  info.append((solve, year, name))

info.sort(key=lambda x: x[1])
team_name1 = ''

for i in range(3):
  team_name1 += info[i][1][-2:]

info.sort(key=lambda x: -int(x[0]))
team_name2 = ''
for i in range(3):
  team_name2 += info[i][2][:1]

print(team_name1)
print(team_name2)