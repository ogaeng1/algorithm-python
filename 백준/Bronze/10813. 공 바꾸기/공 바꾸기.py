n, m = map(int, input().split())

basket = [i for i in range(1, n+1)]

for _ in range(m):
  bas1, bas2 = map(int, input().split())
  ex = basket[bas1-1]
  basket[bas1-1] = basket[bas2-1]
  basket[bas2-1] = ex

for i in basket:
  print(i, end=' ')