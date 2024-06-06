import sys
input = sys.stdin.readline

N = int(input())
x = list(map(int, input().split()))

sort_arr = sorted(list(set(x)))
info = {sort_arr[i]:i for i in range(len(sort_arr))}

for i in x:
  print(info[i], end=' ')