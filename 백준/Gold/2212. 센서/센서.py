import sys
input = sys.stdin.readline

sensor = int(input())
k = int(input())
pos = list(map(int, input().split()))
pos.sort()
dist = []

for i in range(sensor-1):
  dist.append(pos[i+1]-pos[i])
dist.sort()

res = sum(dist[:sensor-k])
print(res)