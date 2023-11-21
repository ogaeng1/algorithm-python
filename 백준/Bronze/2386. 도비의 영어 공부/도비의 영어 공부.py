while True:
  dobby = input().lower()
  if dobby == "#":
    break
  alpha = dobby[0]
  sentence = dobby[2::]
  cnt = sentence.count(alpha)
  print(alpha, cnt)