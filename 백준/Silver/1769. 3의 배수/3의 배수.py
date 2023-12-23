x = input()
cnt = 0

while len(x) > 1:
  total = 0
  for i in range(len(x)):
    total += int(x[i])

  x = str(total)
  cnt += 1
  
print(cnt)
print("YES" if int(x) % 3 == 0 else "NO")