n = int(input())
w = list(map(int, input().split()))
team1, team2 = sorted(w), sorted(w, reverse=True)
res = []

for i in range(n):
  coding = team1[i]+team2[i]
  res.append(coding)

print(min(res))