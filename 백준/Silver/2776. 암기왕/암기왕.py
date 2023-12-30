def binary_search(arr, target):
  start, end = 0, len(arr) - 1

  while start <= end:
    mid = (start + end) // 2
    if arr[mid] == target:
      return 1
    elif arr[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
      
  return 0

t = int(input())

for _ in range(t):
  n = int(input())
  n_list = list(map(int, input().split()))
  m = int(input())
  m_list = list(map(int, input().split()))
  
  n_list.sort()
  
  for i in m_list:
    result = binary_search(n_list, i)
    print(result)