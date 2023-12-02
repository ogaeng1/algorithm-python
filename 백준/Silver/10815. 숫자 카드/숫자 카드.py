def bi_search(n_list, target):
  start, end = 0, len(n_list) - 1
  while start <= end:
    mid = (start + end) // 2
    if n_list[mid] == target:
      return 1
    elif n_list[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return 0

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

for i in m_list:
  res = bi_search(n_list, i)
  print(res)