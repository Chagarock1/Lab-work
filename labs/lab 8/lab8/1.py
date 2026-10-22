try:
    attended = int(input("Введіть кількість присутніх занять: "))
    total = int(input("Введіть загальну кількість занять: "))

    percentage = (attended / total) * 100

    if attended < 0 or total < 0:
        raise ValueError("Кількість занять не може бути від'ємною!")
    if attended > total:
        raise ValueError(
            "Кількість присутніх занять не може перевищувати загальну кількість!"
        )

except ValueError as e:
    print(f"Помилка даних: {e}")
except ZeroDivisionError:
    print("Помилка обчислення: Загальна кількість занять не може дорівнювати 0")
else:
    print(f"Відсоток присутності: {percentage:.1f}%")
