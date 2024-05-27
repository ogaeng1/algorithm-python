import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
  n = int(sys.stdin.readline().strip())
  phone_list = []
  
  for _ in range(n):
    phone_list.append(sys.stdin.readline().strip())

  phone_list.sort()
  bol = True

  for i in range(n-1):
    if phone_list[i+1].startswith(phone_list[i]):
      bol = False
      break

  print('YES' if bol else 'NO')
    