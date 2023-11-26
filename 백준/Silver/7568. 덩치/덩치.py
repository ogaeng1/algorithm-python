N = int(input())
student = []

for _ in range(N):
  weight, height = map(int, input().split())
  student.append((weight, height))

for i in student:
  big = 1
  for j in student:
    if i[0] < j[0] and i[1] < j[1]:
      big += 1
  print(big, end=" ")