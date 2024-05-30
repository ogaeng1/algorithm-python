A, B = map(int, input().split())

num = [i for i in range(1, B+1) for j in range(i)]

print(sum(num[A-1:B]))