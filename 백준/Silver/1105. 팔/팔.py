l, r = map(str, input().split())
cnt = 0

if len(l) != len(r):
  print(0)
else:
  for i in range(len(l)):
    if l[i] == r[i]:
      if l[i] == '8':
        cnt += 1
    else:
      break
  print(cnt)