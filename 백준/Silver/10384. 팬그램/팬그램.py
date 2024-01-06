for _ in range(int(input())):
    s = input()
    s = s.lower()
    arr = [0]*26
    for i in s:
        if i.isalpha():
            arr[ord(i)-97]+=1
    if min(arr)>=3: print("Case %d: Triple pangram!!!"%(_+1))
    elif min(arr)>=2: print("Case %d: Double pangram!!"%(_+1))
    elif min(arr)>=1: print("Case %d: Pangram!"%(_+1))
    else :print("Case %d: Not a pangram"%(_+1))