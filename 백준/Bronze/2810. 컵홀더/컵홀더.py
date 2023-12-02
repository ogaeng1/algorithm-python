n = int(input())
cupholder = input()
couple = cupholder.count('LL')

if cupholder.count('LL') <= 1:
    print(n)
else:
    print(n+1-couple)