A, B = map(int, input().split())
cnt = 0

if A == B:
  print(cnt)
  print(" ")
elif A < B:
  cnt = B-A-1
  print(cnt)
  for i in range(A+1, B):
    print(i, end=" ")
else:
  cnt = A-B-1
  print(cnt)
  for i in range(B+1, A):
    print(i, end=" ")