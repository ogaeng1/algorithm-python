import sys
input = sys.stdin.readline

n = int(input())
crane_weight = list(map(int, input().split()))
m = int(input())
box_weight = list(map(int, input().split()))

crane_weight.sort(reverse=True)
box_weight.sort(reverse=True)

cnt = 0

if crane_weight[0] < box_weight[0]:
  cnt = -1
else:
  while box_weight:
    for crane in crane_weight:
      if box_weight and crane < box_weight[-1]:
        continue
      for box in box_weight:
        if crane >= box:
          box_weight.remove(box)
          break
    cnt += 1

print(cnt)