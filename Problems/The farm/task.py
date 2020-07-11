user_money = int(input())
if user_money >= 6769:
    print(user_money // 6769, "sheep")
elif user_money >= 3848:
    print("1 cow")
elif user_money >= 1296:
    if user_money // 1296 > 1:
        print(user_money // 1296, "pigs")
    else:
        print("1 pig")
elif user_money >= 678:
    print("1 goat")
elif user_money >= 23:
    if user_money // 23 > 1:
        print(user_money // 23, "chickens")
    else:
        print("1 chicken")
else:
    print("None")
