statuses = ["Увімкнено", "Вимкнено", "В очікуванні", "Помилка"]
print(f"Поточний список статусів (індекси від 0 до {len(statuses) - 1}):")
print(statuses)

try:
    index = int(input("Введіть індекс пристрою для зміни: "))
    new_status = input("Введіть новий статус: ").strip()

    if not new_status:
        raise ValueError("Статус не може бути порожнім рядком!")

    statuses[index] = new_status

except ValueError as e:
    print(
        f"Помилка введення: Введіть коректне ціле число для індексу та не порожній статус. ({e})"
    )
except IndexError:
    print(
        f"Помилка індексу: Пристрою з таким індексом не існує! Доступні індекси від 0 до {len(statuses) - 1}."
    )
else:
    print("Статус успішно оновлено!")
    print("Новий список статусів:", statuses)
