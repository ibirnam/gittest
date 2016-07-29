def factorial(x):
    if (x < 2):
        return 1
    elif (x > 1):
        print("Hahaha! I broke your code Ian! >:)")
    else:
        return (x * (factorial(x-1)))
