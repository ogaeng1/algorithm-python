t = int(input())

school = []

for i in range(t):
  n = int(input())
  for _ in range(n):
    school.append((input().split()))
    school.sort(key=lambda x : -int(x[1]))
  print(school[i][0])