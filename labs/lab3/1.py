def calc_sum(n, skip):
    total = 0
    for i in range(1, n + 1):
        if i % skip != 0:
            total = total + i
    return total

skip_number = 3
results = []

for n in range(10, 41, 10):
    res = calc_sum(n, skip_number)
    results.append(res)
    print("При n =", n, "сума дорівнює:", res)

if results[-1] > results[0]:
    print("Сума зростає зі збільшенням n")
