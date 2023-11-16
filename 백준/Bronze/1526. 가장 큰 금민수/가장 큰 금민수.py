N = int(input())

while True:
  gold_minsu = True
  for i in str(N):
    if i!="4" and i!="7":
      gold_minsu = False
      N -= 1
      
  if gold_minsu:
    print(N)
    break