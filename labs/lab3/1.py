def sum(n, skip):
    total = 0
    for i in range(1, n + 1):
        if i % skip != 0:
            total = total + i
    return total

skip_number = 3

for n in [10, 15, 20]:
    result = sum(n, skip_number)
    print("При n =", n, "сума дорівнює:", result)
