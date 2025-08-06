import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt 
category=np.random.choice(['A','B','C'],size=100)
value=np.random.randn(100)
sns.boxplot(x=category,y=value)
plt.show()

