n = int(input())
B = list(map(int, input().split()))

res = 0

while True:
  for i in range(n):
    if B[i] % 2:
      B[i] -= 1
      res += 1
      
  if sum(B) == 0:
    break
  
  for i in range(n):
    B[i] //= 2
  res += 1

print(res)