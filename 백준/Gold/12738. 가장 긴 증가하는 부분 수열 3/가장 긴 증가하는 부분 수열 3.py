from bisect import bisect_left

n = int(input())
A = list(map(int, input().split()))
arr = []

for i in A:
  idx = bisect_left(arr, i)
  if len(arr) == idx:
    arr.append(i)
  else:
    arr[idx] = i

print(len(arr))