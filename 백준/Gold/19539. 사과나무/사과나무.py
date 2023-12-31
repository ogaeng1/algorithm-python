n = int(input())
height = list(map(int, input().split()))

res = 0
if sum(height) % 3 == 0:
  for i in height:
    res += i // 2
  if res >= (sum(height) // 3):
    print("YES")
  else:
    print("NO")
else:
  print("NO")