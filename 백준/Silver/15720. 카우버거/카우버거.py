b, c, d = map(int,input().split())

burger = sorted(list(map(int, input().split())), reverse=True)
side = sorted(list(map(int, input().split())), reverse=True)
drink = sorted(list(map(int, input().split())), reverse=True)

before_sum = sum(burger) + sum(side) + sum(drink)

set_menu = min(len(burger), len(side), len(drink))

discount_price = before_sum - (sum(burger[:set_menu]) + sum(side[:set_menu]) + sum(drink[:set_menu])) // 10

print(before_sum)
print(discount_price)