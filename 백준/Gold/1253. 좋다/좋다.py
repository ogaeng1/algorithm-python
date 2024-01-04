n = int(input())
arr = list(map(int, input().split()))

arr.sort()
cnt = 0

for i in range(n):
  start, end = 0, len(arr) - 1
  target = arr[i]

  while start < end:
    if arr[start] + arr[end] == target:
      if start == i:
        start += 1
      elif end == i:
        end -= 1
      else:
        cnt += 1
        break
    elif arr[start] + arr[end] < target:
      start += 1
    elif arr[start] + arr[end] > target:
      end -= 1

print(cnt)