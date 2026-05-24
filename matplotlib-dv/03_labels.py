import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([17, 23, 38, 5])
y3 = np.array([13, 15, 20, 30])


# LABELS
plt.title("Class size",
          fontsize=25,
          family="Arial",
          fontweight="bold",
          color="#2d4cfc")

plt.xlabel("Year",
           fontsize=20,
           fontfamily="Arial",
           fontweight="bold",
           color="#2db3fc")

plt.ylabel("Students",
           fontsize=20,
           fontfamily="Arial",
           fontweight="bold",
           color="#2db3fc")

plt.tick_params(axis="both",
                colors="#2db3fc")  # here colors as plural

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

# force the interval in x to be specific
plt.xticks(x)

plt.show()
