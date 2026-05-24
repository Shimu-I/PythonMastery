# Histogram = A visual representation of the distribution of quantitative data.
#             They group values into bins (intervals)
#             and counts how many fail in each range.

import matplotlib.pyplot as plt
import numpy as np

# loc = location of median of data
# scale = standard deviation or spread -- higher the number greater the deviation

scores = np.random.normal(loc=80, scale=10, size=100)
scores = np.clip(scores, 0, 100)

# bins = rectangular
plt.hist(scores, bins=10, color="lightgreen",
         edgecolor="black")

plt.title("Exam Scores")
plt.xlabel("Score")
plt.ylabel("# of students")
plt.show()