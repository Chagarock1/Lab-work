def suma(n, k):
    s = 0

    for i in range(1, n + 1):
        if i % k != 0:
            s += i

    return s


n = int(input("Введіть n: "))
k = int(input("Введіть число, кратні якому пропускати: "))

print("Сума:", suma(n, k))
