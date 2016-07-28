def factorial(x):
    if (x < 2):
        return 1
    elif (x > 10000):
        print("HAHAHAHA!")
    else:
        return (x * (factorial(x-1)))
