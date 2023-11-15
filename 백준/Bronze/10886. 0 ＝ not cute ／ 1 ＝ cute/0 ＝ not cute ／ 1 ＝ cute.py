N = int(input())
arr = []

for i in range(N):
  vote = int(input())
  arr.append(vote)

if arr.count(0) > arr.count(1):
  print("Junhee is not cute!")
else:
  print("Junhee is cute!")