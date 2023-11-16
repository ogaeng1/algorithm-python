T = int(input())

for i in range(1, T+1):
  dice1, dice2 = map(int, input().split())
  print(f"Case {i}: {dice1+dice2}")