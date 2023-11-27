N, L = map(int, input().split())
h = list(map(int, input().split()))

height = sorted(h)

for i in height:
  if L >= i:
    L += 1
  else:
    break

print(L)