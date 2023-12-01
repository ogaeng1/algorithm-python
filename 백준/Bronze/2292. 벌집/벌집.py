n = int(input())

bee = 1
cur = 1

while n > bee:
    bee += 6*cur
    cur += 1
    
print(cur)