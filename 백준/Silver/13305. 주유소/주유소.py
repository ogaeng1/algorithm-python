import sys
input = sys.stdin.readline

n = int(input())
city_distance = list(map(int, input().split()))
oil_price = list(map(int, input().split()))

cheapest = oil_price[0]
price = 0

for i in range(n-1):
  if cheapest > oil_price[i]:
    cheapest = oil_price[i]
  price += cheapest * city_distance[i]
    
print(price)