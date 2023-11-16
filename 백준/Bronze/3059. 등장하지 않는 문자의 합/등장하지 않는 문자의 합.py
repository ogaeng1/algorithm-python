alpha = {'A', 'B', 'C', 'D', 'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}

T = int(input())

for _ in range(T):
  sum = 0
  input_set = set(input())
  cha_set = set(alpha - input_set)
  for i in cha_set:
    sum += ord(i)
  print(sum)