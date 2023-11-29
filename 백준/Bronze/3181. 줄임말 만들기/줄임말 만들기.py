text = input().split()
str_list = {'i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili'}

new_str = ''

for word in text:
    if word in str_list and new_str == '':
        new_str += word[0]
    elif word not in str_list:
        new_str += word[0]

print(new_str.upper())