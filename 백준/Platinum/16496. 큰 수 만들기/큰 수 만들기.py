from functools import cmp_to_key

n = int(input())
num_list = list(input().split())

def compare(x, y):
  if x+y > y+x:
    return -1
  elif x+y < y+x:
    return 1
  else:
    return 0

num_list.sort(key = cmp_to_key(compare))

cnt = 0
for i in num_list:
  if i == '0':
    cnt += 1

if cnt == len(num_list):
  print(0)
else:
  print(''.join(num_list))