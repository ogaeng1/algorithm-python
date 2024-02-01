s = input()
arr = s.split('-')

cal = sum(map(int, arr[0].split('+')))
for i in arr[1:]:
    cal -= sum(map(int, i.split('+')))
    
print(cal)