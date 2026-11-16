import matplotlib.pyplot as plt
import pandas as pd

sample_csv = """Дата,Офіційний курс гривні, грн
18.10.2026,0.000495
22.10.2026,0.000498
26.10.2026,0.000501
30.10.2026,0.000500
03.11.2026,0.000504
07.11.2026,0.000502
11.11.2026,0.000505
14.11.2026,0.000508
17.11.2026,0.000506
"""

with open("kurs.csv", "w", encoding="utf-8") as f:
    f.write(sample_csv)

f = pd.read_csv("kurs.csv")

f["Дата"] = pd.to_datetime(f["Дата"], format="%d.%m.%Y")

plt.plot(f["Дата"], f["Офіційний курс гривні, грн"], color="blue", marker="o", label="Курс LBP/UAH")
plt.title("Офіційний курс ліванського фунта (LBP) за останній місяць")
plt.xlabel("Дата")
plt.ylabel("Курс, грн")
plt.legend(loc="upper left")
plt.grid(True, linestyle="--", alpha=0.6)
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.savefig("currency_rate.png", dpi=150)
plt.show()
