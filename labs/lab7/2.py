living_room_devices = {
    "Телевізор",
    "Лампа",
    "Кондиціонер",
    "Аудіосистема",
    "Розумна розетка"
}

all_turned_on_devices = {
    "Лампа",
    "Аудіосистема",
    "Бойлер",
    "Розумна розетка",
    "Холодильник"
}

turned_on_in_living_room = living_room_devices.intersection(all_turned_on_devices)

turned_off_in_living_room = living_room_devices.difference(all_turned_on_devices)

print("Пристрої у вітальні:", living_room_devices)
print("Усі увімкнені пристрої в будинку:", all_turned_on_devices)
print("-" * 50)

print("1. Увімкнені пристрої у вітальні:")
for device in turned_on_in_living_room:
    print(f"  - {device}")

print("\n2. Вимкнені пристрої у вітальні:")
for device in turned_off_in_living_room:
    print(f"  - {device}")
