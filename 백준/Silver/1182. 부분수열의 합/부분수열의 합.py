import sys
input = sys.stdin.readline

def backtracking(n):
  cnt = 0
  if sum(arr) == S and len(arr) > 0:
    cnt += 1

  for i in range(n, len(seq)):
    arr.append(seq[i])
    cnt += backtracking(i+1)
    arr.pop()

  return cnt

N, S = map(int, input().split())
seq = list(map(int, input().split()))
arr = []

print(backtracking(0))