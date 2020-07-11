# write your code here
import math
import argparse


# cp - credit principal
# mp - monthly payment
# np - number of payments
# ci - credit interest
# m - current period

def differentiate_payment(cp, ci, np, m):
    return math.ceil(cp / np + ci / 12 * (cp - cp * (m - 1) / np))


def annuity_payment(cp, ci, np):
    return math.ceil(cp \
           * (ci / 12 * math.pow(1 + ci / 12, np)) \
           / (math.pow(1 + ci / 12, np) - 1))


def credit_principal(mp, ci, np):
    return math.ceil(mp \
           * (math.pow(1 + ci / 12, np) - 1) \
           / (math.pow(1 + ci / 12, np) * ci / 12))


def number_of_payments(cp, mp, ci):
    return math.ceil(math.log(mp / (mp - ci / 12 * cp), 1 + ci / 12))


parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment", type=int)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
args = parser.parse_args()

none_count = 0
is_negative = False
for item in [args.type, args.payment, args.principal, args.periods, args.interest]:
    if item is None:
        none_count += 1
    if type(item) == int and item < 0:
        is_negative = True

total_payments = 0
if args.type not in ["annuity", "diff"] or args.type == "diff" and args.payment is not None \
        or none_count > 1 or is_negative:
    print("Incorrect parameters")
elif args.type == "annuity":
    if args.payment is None:
        user_payment = annuity_payment(args.principal, args.interest / 100, args.periods)
        print(f"Your annuity payment = {user_payment}!")
        total_payments = user_payment * args.periods
        print(f"Overpayment = {total_payments - args.principal}")
    if args.principal is None:
        user_principal = credit_principal(args.payment, args.interest / 100, args.periods)
        print(f"Your credit principal = {user_principal}!")
        total_payments = args.payment * args.periods
        print(f"Overpayment = {total_payments - user_principal}")
    if args.periods is None:
        user_periods = number_of_payments(args.principal, args.payment, args.interest / 100)
        if user_periods % 12 == 0:
            print(f"You need {user_periods // 12} years to repay this credit!")
        elif user_periods < 12:
            print(f"You need {user_periods} months to repay this credit!")
        else:
            print(f"You need {user_periods // 12} years and {user_periods % 12} months to repay this credit!")
        total_payments = args.payment * user_periods
        print(f"Overpayment = {total_payments - args.principal}")
else:
    for current_month in range(1, args.periods + 1):
        total_payments += differentiate_payment(args.principal, args.interest / 100, args.periods, current_month)
        print(f"Month {current_month}: "
              f"paid out {differentiate_payment(args.principal, args.interest / 100, args.periods, current_month)}")
    print()
    print(f"Overpayment = {total_payments - args.principal}")
