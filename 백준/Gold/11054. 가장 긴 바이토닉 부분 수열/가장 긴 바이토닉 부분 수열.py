import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split())) 

r_arr = arr[::-1] 

increase = [1]*n
decrease = [1]*n

for i in range(n):
  for j in range(i):
    if arr[i] > arr[j]:
      increase[i] = max(increase[i], increase[j]+1)
    if r_arr[i] > r_arr[j]:
      decrease[i] = max(decrease[i], decrease[j]+1)

decrease = decrease[::-1]

res = []
for i in range(n):
  res.append(decrease[i] + increase[i]-1)

print(max(res))