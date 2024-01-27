from sys import stdin

n = int(stdin.readline())
solution = list(map(int, stdin.readline().split()))

start, end = 0, n-1
mid = abs(solution[start] + solution[end])
res = [solution[start], solution[end]]

while start < end:
  target = solution[start] + solution[end]

  if abs(target) < mid:
    mid = abs(target)
    res = [solution[start], solution[end]]

    if mid == 0:
      break

  if target < 0:
    start += 1
  else:
    end -= 1

print(res[0], res[1])