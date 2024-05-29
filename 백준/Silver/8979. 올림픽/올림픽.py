N, K = map(int, input().split())
country = []
rank = 1

for _ in range(N):
  c, g, s, b = map(int, input().split())
  country.append((c,g,s,b))

country.sort(key=lambda x: (-x[1], -x[2], -x[3]))

for i, (c,g,s,b) in enumerate(country):
  if c == K:
    print(rank)
    break

  if i < N - 1 and (g, s, b) != (country[i+1][1], country[i+1][2], country[i+1][3]):
    rank = i + 2