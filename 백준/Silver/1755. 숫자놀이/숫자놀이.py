def convert_english(num):
  return ' '.join(english_num[i] for i in str(num))

M, N = map(int, input().split())
english_num = {
  '0': 'zero',
  '1': 'one',
  '2': 'two',
  '3': 'three',
  '4': 'four',
  '5': 'five',
  '6': 'six',
  '7': 'seven',
  '8': 'eight',
  '9': 'nine'
}

convert_result = [(i, convert_english(i)) for i in range(M, N+1)]
convert_result.sort(key=lambda x: x[1])

for i, (num, eng) in enumerate(convert_result):
  if i > 0 and i % 10 == 0:
    print()
  print(num, end=' ')