l = int(input())
r = int(input())

branch = 0
cnt = 1

while True:
  l = int(l * (r / 100))

  if l <= 5:
    break
  branch += (2 ** cnt) * l
  cnt += 1
  
print(branch)