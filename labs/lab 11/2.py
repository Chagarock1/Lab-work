import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-6, -2.2, 150)
y1 = 1 / (x1 + 2)

x2 = np.linspace(-1.8, 4, 150)
y2 = 1 / (x2 + 2)

plt.plot(x1, y1, color="blue", label="y = 1 / (x + 2)")
plt.plot(x2, y2, color="blue")

plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.axvline(-2, color="red", linestyle="--", linewidth=0.9, label="Асимптота (x = -2)")

plt.title("Графік функції y = 1 / (x + 2)")
plt.xlabel("x")
plt.ylabel("y")
plt.ylim(-10, 10)
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig("hyperbola_chart.png", dpi=150)
plt.show()
