N = int(input())

for _ in range(N):
  nickname = input().split()
  god = nickname[0].replace(nickname[0], "god")
  name = "".join(nickname[1::])
  print(god+name)