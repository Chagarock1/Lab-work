import matplotlib.pyplot as plt

event_types = ["DEBUG", "INFO", "WARNING", "ERROR"]
event_counts = [150, 95, 30, 12]

plt.bar(event_types, event_counts, color=["skyblue", "lightgreen", "orange", "salmon"])

plt.title("Розподіл подій у журналі за категоріями")
plt.xlabel("Тип події")
plt.ylabel("Кількість подій, шт.")
plt.grid(True, axis="y", linestyle="--", alpha=0.7)

plt.tight_layout()
plt.savefig("events_chart.png", dpi=150)
plt.show()
