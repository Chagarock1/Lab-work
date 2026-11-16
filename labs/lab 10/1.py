flights = [
    "PS-101",
    "TK-452",
    "LH-1490",
    "FR-2341",
    "W6-6123",
    "KL-1385",
    "AF-1752",
    "BA-882",
    "LO-751",
    "OS-661"
]

with open("flights_numbers.txt", "w", encoding="utf-8") as file:
    for flight in flights:
        file.write(flight + "\n")

loaded_flights = []
with open("flights_numbers.txt", "r", encoding="utf-8") as file:
    for line in file:
        loaded_flights.append(line.strip())

print("Номери рейсів у зворотному порядку:")
for flight in reversed(loaded_flights):
    print(flight)
