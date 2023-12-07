n = int(input())
chu = list(map(int, input().split()))
chu.sort()

target = 1

for i in chu:
  if target < i:
    break

  target += i

print(target)