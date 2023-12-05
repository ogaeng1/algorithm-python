x = int(input())
line = 1

while x > line:
  x -= line
  line += 1

if line % 2 == 0:
  deno = x
  numer = line - x + 1
else:
  deno = line - x + 1
  numer = x

print(f'{deno}/{numer}')