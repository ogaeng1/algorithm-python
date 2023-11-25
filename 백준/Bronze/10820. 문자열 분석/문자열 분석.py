import sys
while True:
  N = sys.stdin.readline().rstrip("\n")

  if not N:
    break
  lower, upper, number, gap = 0, 0, 0, 0

  for i in N:
    if i.islower():
      lower += 1
    elif i.isupper():
      upper += 1
    elif i.isdigit():
      number += 1
    elif i.isspace():
      gap += 1
  print(lower, upper, number, gap)