initial_data = [
    "PS-101;Варшава;08:30;15",
    "TK-452;Стамбул;10:15;5",
    "LH-1490;Франкфурт;11:45;28",
    "FR-2341;Краків;13:00;0",
    "W6-6123;Будапешт;14:20;42",
    "KL-1385;Амстердам;16:05;12",
    "AF-1752;Париж;17:50;3",
    "BA-882;Лондон;19:10;30",
    "LO-751;Варшава;20:40;8",
    "OS-661;Відень;22:00;19"
]

with open("flights.txt", "w", encoding="utf-8") as file:
    for record in initial_data:
        file.write(record + "\n")

min_seats = int(input("Введіть мінімальну кількість вільних місць: "))

print(f"\nРейси, на які є не менше ніж {min_seats} вільних місць:")

with open("flights.txt", "r", encoding="utf-8") as source, \
     open("available_flights.txt", "w", encoding="utf-8") as result:
    
    for line in source:
        flight, destination, time, free_seats = line.strip().split(";")

        if int(free_seats) >= min_seats:
            print(f"Рейс: {flight} | Пункт: {destination} | Час: {time} | Вільних місць: {free_seats}")
            result.write(line)

print("\nРезультати успішно збережено у файл available_flights.txt")
