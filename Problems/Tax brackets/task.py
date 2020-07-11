user_income = int(input())
percent = 0
if user_income <= 15527:
    percent = 0
elif 15528 <= user_income <= 42707:
    percent = 15
elif 42708 <= user_income <= 132406:
    percent = 25
else:
    percent = 28
calculated_tax = user_income * percent / 100
print(f"The tax for {user_income} is {percent}%. That is {calculated_tax:.0f} dollars!")
