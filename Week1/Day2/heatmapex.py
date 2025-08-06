import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Create 5x5 matrix of random values
data = np.random.rand(5, 5)

# Create heatmap
sns.heatmap(data, annot=True, cmap='viridis')

plt.title("Heatmap Example (Random Data)")
plt.show()
