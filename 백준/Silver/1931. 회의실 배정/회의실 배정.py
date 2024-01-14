n = int(input())
meet = [list(map(int, input().split())) for _ in range(n)]

meet.sort(key=lambda x: (x[1], x[0]))

end_time = 0
res = 0

for i in meet:
  start, end = i

  if start >= end_time:
    res += 1
    end_time = end

print(res)