n = int(input())
arr = []

for _ in range(n):
  name = input()
  arr.append(name)

if arr == sorted(arr):
  print("INCREASING")
elif arr == sorted(arr, reverse=True):
  print("DECREASING")
else:
  print("NEITHER")