def f(n):
    if n == 0:
        return 0
    elif n > 0:
        return f(n - 1) + 3
    else:
        return 0

n = int(input("Введіть n: "))
print(f(n))
