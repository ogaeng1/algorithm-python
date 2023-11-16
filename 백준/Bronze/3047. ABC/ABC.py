A, B, C = map(int, input().split())
A, B, C = sorted((A, B, C))
alpha = input()

for i in alpha:
  if i == "A":
    print(A, end=" ")
  elif i == "B":
    print(B, end=" ")
  else:
    print(C, end=" ")