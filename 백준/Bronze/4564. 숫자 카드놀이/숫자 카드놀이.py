while True:
  S = input() 
  if S == "0":
    break
  while len(S) > 1:
    result = 1
    print(S, end=" ")
    for i in S:
      result *= int(i)
    S = str(result)
  print(S)