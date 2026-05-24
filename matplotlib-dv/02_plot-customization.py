import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([17, 23, 38, 5])
y3 = np.array([13, 15, 20, 30])
line_style = dict(
    marker=".", 
    ms=30, 
    mfc="#1cd3fc",
    mec="red", 
    linestyle="solid", 
    linewidth=4

)


# plot(x axis,
# y axis,
# marker sign(dot = ".", circle = "o", triangle = "v", star = "*"),
# markersize = ms,
# markerfacecolor = mfc,
# markeredgecolor = mec,
# linestyle(default=solid) (dashed, dotted, dashdot, None),
# linewidth (nomally is 1),
# color (line color)
# )

# read matplot document for more markers


plt.plot(x, y1, color="#1c5bfc", **line_style)

plt.plot(x, y2, color="#1cfc45",  **line_style)

plt.plot(x, y3, **line_style,  color="#fc1c1c")


# how do we make the y2 style as y1
# not recommended = copy paste form the y1
# recommented = create a dictionarly for the style
# to have different color of each line first remove the color style form the dict then add different color to the plt.plot(color=)

plt.show()


