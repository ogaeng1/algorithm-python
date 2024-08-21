import sys
input = sys.stdin.readline

N = int(input())
p_num = []
n_num = []
zero = 0
res = 0

for _ in range(N):
  n = int(input())
  if n < 0:
    n_num.append(n)
  elif n == 1:
    res += n
  elif n == 0:
    zero += 1
  elif n > 1:
    p_num.append(n)

p_num.sort(reverse=True)
n_num.sort()

for i in range(0, len(p_num)-1, 2):
  res += p_num[i] * p_num[i+1]
if len(p_num) % 2 == 1:
  res += p_num[-1]

for i in range(0, len(n_num)-1, 2):
  res += n_num[i] * n_num[i+1]
if len(n_num) % 2 == 1:
  if zero == 0:
    res += n_num[-1]

print(res)