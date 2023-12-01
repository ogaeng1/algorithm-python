t = int(input())

APT = [[0] * 14 for _ in range(15)]

for i in range(14):
  APT[0][i] = i + 1

for i in range(1, 15):
  for j in range(14):
    APT[i][j] = sum(APT[i-1][:j+1])

for _ in range(t):
  k = int(input())
  n = int(input())
  print(APT[k][n-1])