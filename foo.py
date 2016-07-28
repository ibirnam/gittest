def factorial(x):
    if (x < 2):
        return 0
    else:
        return (x * (factorial(x-1)))