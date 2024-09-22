import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split())) + [0, 0]
res = 0

for i in range(n):
  if arr[i+1] > arr[i+2]:
    price = min(arr[i], arr[i+1]-arr[i+2])
    arr[i] -= price
    arr[i+1] -= price
    res += price * 5

    price = min(arr[i], arr[i+1], arr[i+2])
    arr[i] -= price
    arr[i+1] -= price
    arr[i+2] -= price
    res += price * 7
  else:
    price = min(arr[i], arr[i+1], arr[i+2])
    arr[i] -= price
    arr[i+1] -= price
    arr[i+2] -= price
    res += price * 7

    price = min(arr[i], arr[i+1])
    arr[i] -= price
    arr[i+1] -= price
    res += price * 5

  res += arr[i] * 3
  arr[i] = 0

print(res)