N, K = map(int, input().split())
num = []

for i in range(1, K+1):
  num.append(int(str(N*i)[::-1]))

print(max(num))