A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_score, B_score = 0, 0

for i in range(10):
  if A[i] > B[i]:
    A_score += 1
  elif A[i] < B[i]:
    B_score += 1

if A_score > B_score:
  print("A")
elif A_score < B_score:
  print("B")
else:
  print("D")