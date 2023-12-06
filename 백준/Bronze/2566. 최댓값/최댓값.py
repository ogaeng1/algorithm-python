max_val, row, col = 0, 0, 0
arr = []

for i in range(9):
  num = list(map(int, input().split()))
  arr.append(num)

  for j in range(9):
    if num[j] > max_val:
      max_val = num[j]
      row, col = i, j

print(max_val)
print(row+1, col+1)