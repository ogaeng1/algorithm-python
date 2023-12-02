n = int(input())
student = []

for _ in range(n):
  name, day, month, year = input().split()
  student.append([name, int(day), int(month), int(year)])

student.sort(key=lambda x: (x[3], x[2], x[1]))

print(student[-1][0])
print(student[0][0])