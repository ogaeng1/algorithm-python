N = int(input())
human = list(map(int, input().split()))
human.sort()

time, total = 0, 0

for i in human:
  time += i
  total += time
print(total)