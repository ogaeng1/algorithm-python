from sys import stdin
from bisect import bisect_left

n = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
arr, temp = [], []

for i in A:
  if not arr or arr[-1] < i:
    arr.append(i)
    temp.append((len(arr)-1, i))
  else:
    arr[bisect_left(arr, i)] = i
    temp.append((bisect_left(arr, i), i))

res = []
idx = len(arr)-1

for i in range(len(temp)-1, -1, -1):
  if temp[i][0] == idx:
    res.append(temp[i][1])
    idx -= 1

print(len(arr))
print(*res[::-1])