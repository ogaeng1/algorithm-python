N = int(input())
result = 1

for i in range(1, N+1):
  result *= i

result = str(result)[::-1]
cnt = 0

for i in result:
  if i != "0":
    break
  if i == "0":
    cnt += 1

print(cnt)