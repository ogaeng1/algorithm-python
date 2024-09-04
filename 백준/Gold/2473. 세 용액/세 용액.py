import sys
input = sys.stdin.readline

n = int(input())
solution = list(map(int, input().split()))
solution.sort()

init = float('inf')
res = []

for i in range(n-2):
  left, right = i+1, n-1

  while left < right:
    cur = solution[i] + solution[left] + solution[right]

    if abs(cur) < abs(init):
      init = cur
      res = [solution[i], solution[left], solution[right]]

    if cur < 0:
      left += 1
    elif cur > 0:
      right -= 1
    else:
      break

print(' '.join(map(str, sorted(res))))