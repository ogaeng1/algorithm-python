score = 0
sum = 0

for _  in range(20):
  info = input().split()
  if info[2] == "A+":
    score += float(info[1]) * 4.5
    sum += float(info[1])
  elif info[2] == "A0":
    score += float(info[1]) * 4
    sum += float(info[1])
  elif info[2] == "B+":
    score += float(info[1]) * 3.5
    sum += float(info[1])
  elif info[2] == "B0":
    score += float(info[1]) * 3
    sum += float(info[1])
  elif info[2] == "C+":
    score += float(info[1]) * 2.5
    sum += float(info[1])
  elif info[2] == "C0":
    score += float(info[1]) * 2
    sum += float(info[1])
  elif info[2] == "D+":
    score += float(info[1]) * 1.5
    sum += float(info[1])
  elif info[2] == "D0":
    score += float(info[1]) * 1.0
    sum += float(info[1])
  elif info[2] == "F":
    score += 0
    sum += float(info[1])
  elif info[2] == "P":
    continue

print(score / sum)