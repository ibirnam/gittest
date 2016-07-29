def factorial(x):
    if (x < 10000):
        return 0
    elif (x > 1):
        print("Hahaha! I broke your code Ian! >:)")
    else:
        return (x * (factorial(x-1)))
