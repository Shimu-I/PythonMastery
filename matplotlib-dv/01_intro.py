import matplotlib.pyplot as plt
import numpy as np

# print(matplotlib.__version__)

# pyplot lines inside of matplotlib
# provides a user-friendly interface for plotting


# ===========================
# Python normal array
# ===========================
x = [2023, 2024, 2025, 2026]
y = [15, 25, 30, 20]

# x = x axis
# y = y axis

# plt.plot(x, y)
# plt.show()

# ===========================
# Python numpy array -- faster and more functionality
# ===========================

x = np.array([2023, 2024, 2025, 2026])
y = np.array([15, 25, 30, 20])

plt.plot(x, y)
plt.show()
