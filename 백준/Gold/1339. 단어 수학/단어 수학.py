import sys
input = sys.stdin.readline

N = int(input())
word = []

for _ in range(N):
  word.append(list(input().rstrip()))

dict = {}

for i in word:
  x = len(i)-1
  for j in i:
    if j in dict:
      dict[j] += 10**x
    else:
      dict[j] = 10**x
    x -= 1

sort_dict = sorted(dict.values(), reverse=True)
num, res = 9, 0

for i in sort_dict:
  res += i * num
  num -= 1

print(res)