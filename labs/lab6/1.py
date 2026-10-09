input_prices = input("Введіть ціни товарів через пробіл: ").split()
prices = [float(x) for x in input_prices]

p = float(input("Введіть межу p: "))

updated_prices = []
for price in prices:
    if price > p:
        new_price = price * 0.90
    else:
        new_price = price
    updated_prices.append(round(new_price, 2))

print(f"Початковий список цін: {prices}")
print(f"Оновлений список цін: {updated_prices}")
