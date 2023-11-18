N = int(input())
A, B = 0, 0

for _ in range(N):
  score = list(map(int, input().split()))
  if score[0] > score[1]:
    A += 1
  elif score[0] < score[1]:
    B += 1
  else:
    pass

print(A, B)