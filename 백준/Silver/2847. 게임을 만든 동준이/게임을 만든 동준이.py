N = int(input())
score = [int(input()) for _ in range(N)]

cnt = 0

for i in range(N-2, -1, -1):
  if score[i] >= score[i+1]:
    cnt += score[i] - score[i+1] + 1
    score[i] = score[i+1]-1

print(cnt)