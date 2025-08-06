import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt  

data = np.random.randn(100)
sns.histplot(data=data, bins=10)

plt.show()  




