is_multiple_of_10 = lambda x: x % 10 == 0

for number in range(1, 11):
    print(f"Число {number} кратне 10: {is_multiple_of_10(number)}")

for number in range(10, 101, 10):
    print(f"Число {number} кратне 10: {is_multiple_of_10(number)}")
