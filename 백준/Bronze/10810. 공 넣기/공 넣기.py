n, m = map(int, input().split())

basket = [0] * n

for _ in range(m):
  basket1, basket2, ball = map(int, input().split())
  for i in range(basket1-1, basket2):
    basket[i] = ball

for i in basket:
  print(i, end=' ')