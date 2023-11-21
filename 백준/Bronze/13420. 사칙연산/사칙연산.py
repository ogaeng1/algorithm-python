T = int(input())

for _ in range(T):
  cal = input().split()
  a, b, c, res = int(cal[0]), int(cal[2]), int(cal[4]), 0
  oper = cal[1]

  if oper == "+":
    res = a+b
  elif oper == "-":
    res = a-b
  elif oper == "*":
    res = a*b
  elif oper == "/":
    res = a//b

  print("correct" if res == c else "wrong answer")