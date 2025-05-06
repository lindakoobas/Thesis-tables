import matplotlib.pyplot as plt
import pandas as pd

# Lahendamisaeg sekundites
data = {
    "Ülesanne": ["Mäng 1.1", "Mäng 1.2", "Mäng 1.3", "Mäng 1.4", "Mäng 1.5", "Mäng 1.6"],
    "Paber": [43, 28, 33, 55, 70, 95],
    "Telefon": [42, 26, 25, 44, 30, 34]
}

df = pd.DataFrame(data)

# Abifunktsioon sekundite muutmiseks mm:ss formaati
def sec_to_mmss(seconds):
    return f"{seconds // 60:02}:{seconds % 60:02}"

# Graafiku loomine
fig, ax = plt.subplots(figsize=(10, 6))
x = range(len(df))
bar_width = 0.35

# Joonistame tulbad
ax.bar([i - bar_width/2 for i in x], df["Paber"], width=bar_width, label="Paber", color='skyblue')
ax.bar([i + bar_width/2 for i in x], df["Telefon"], width=bar_width, label="Telefon", color='purple')

# Y-telg mm:ss formaadis
yticks = range(0, 110, 15)
ax.set_yticks(yticks)
ax.set_yticklabels([sec_to_mmss(y) for y in yticks])

# Telgede ja pealkirjade seadistamine
ax.set_title("Mäng 1 keskmised lahendamise ajad")
ax.set_ylabel("Lahendamise aeg (mm:ss)")
ax.set_xticks(x)
ax.set_xticklabels(df["Ülesanne"])
ax.legend()

plt.tight_layout()
plt.show()
