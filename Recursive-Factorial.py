def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


print("Factorial of 5 is ..." + str(factorial(5)))
