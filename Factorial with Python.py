def factorial(n):
    fac = 1
    for i in range(n):
        fac = fac * (i + 1)
    return fac

n = int(input('Enter a number'))
print(factorial(n))