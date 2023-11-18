N = int(input())

for _ in range(N):
  num = input()
  sum = int(num) + int(num[::-1])
  if str(sum) == str(sum)[::-1]:
    print("YES")
  else:
    print("NO")