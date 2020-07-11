number_of_iterations = int(input())
for _ in range(number_of_iterations):
    number = int(input())
    if number % 7 == 0:
        print(number ** 2)
