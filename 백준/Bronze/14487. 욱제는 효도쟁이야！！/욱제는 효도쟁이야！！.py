n = int(input())
pay = list(map(int, input().split()))

total = sum(pay)
print(total - max(pay))