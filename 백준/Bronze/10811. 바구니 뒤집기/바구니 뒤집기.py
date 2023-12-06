n, m = map(int, input().split())
basket = [i for i in range(1, n+1)]

for _ in range(m):
  bas1, bas2 = map(int, input().split())
  basket[bas1-1:bas2] = reversed(basket[bas1-1:bas2])

for i in basket:
  print(i, end=' ')