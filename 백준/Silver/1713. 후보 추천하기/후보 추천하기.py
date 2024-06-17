import sys
input = sys.stdin.readline

N = int(input())
recommend = int(input())
student = list(map(int, input().split()))

candidate = {}
for idx, i in enumerate(student):
  if i in candidate:
    candidate[i][2] += 1
  else:
    if len(candidate) == N:
      min_candidate = sorted(list(candidate.values()), key=lambda x: (-x[2], -x[1]))[-1][0]
      del candidate[min_candidate]
    candidate[i] = [i, idx, 1]

res = list(map(str, sorted(candidate.keys())))
print(*res)