S = int(input())
i = 0
num = 0

while True:
  if i < S:
    i += 1
    S -= i
    num += 1
  else:
    print(num)
    break