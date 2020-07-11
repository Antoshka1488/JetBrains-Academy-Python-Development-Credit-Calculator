menu = "pizza, salad, soup"
user_order = input()
if user_order in menu:
    if user_order == "pizza":
        print("Margarita, Four Seasons, Neapoletana, Vegetarian, Spicy")
    elif user_order == "salad":
        print("Caesar salad, Green salad, Tuna salad, Fruit salad")
    else:
        print("Chicken soup, Ramen, Tomato soup, Mushroom cream soup")
else:
    print("Sorry, we don't have it in the menu")
