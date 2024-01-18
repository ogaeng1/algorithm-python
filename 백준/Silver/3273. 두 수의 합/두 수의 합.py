import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

num.sort()
cnt = 0
start, end = 0, n-1

while start < end:
  target = num[start] + num[end]
  
  if target == x:
    cnt += 1
    start += 1
    end -= 1
  elif target < x:
    start += 1
  elif target > x:
    end -= 1

print(cnt)