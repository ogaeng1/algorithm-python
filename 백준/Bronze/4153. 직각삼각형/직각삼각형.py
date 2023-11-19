while True:
  n = list(map(int, input().split()))
  n = sorted(n)
  if n[0] == 0 and n[1] == 0 and n[2] == 0:
    break
  elif n[2]**2 == n[1]**2 + n[0]**2:
    print("right")
  else:
    print("wrong")