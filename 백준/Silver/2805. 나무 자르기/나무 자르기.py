n, m = map(int, input().split())
tree = list(map(int, input().split()))

start, end = 0, max(tree)

while start <= end:
  tree_length = 0
  mid = (start + end) // 2

  for i in tree:
    if i > mid:
      tree_length += i - mid

  if tree_length >= m:
    start = mid + 1
  else:
    end = mid - 1

print(end)