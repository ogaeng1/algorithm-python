n = int(input())
meet = [list(map(int, input().split())) for _ in range(n)]

meet.sort(key=lambda x: (x[1], x[0]))

end_time = 0
res = 0

for i in meet:
  if end_time <= i[0]:
    end_time = i[1]
    res += 1

print(res)