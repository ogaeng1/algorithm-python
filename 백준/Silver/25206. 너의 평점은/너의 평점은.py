score = 0
sum = 0

info = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

for _ in range(20):
    subject, credit, grade = input().split()
    if grade == "P":
        continue
    score += float(credit) * info[grade]
    sum += float(credit)
    
print(score/sum)