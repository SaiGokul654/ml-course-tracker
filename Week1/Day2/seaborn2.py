import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt 
x=np.random.randn(100)
y=np.random.randn(100)
hue=np.random.choice(['A','B'],size=100)
sns.scatterplot(x=x,y=y,hue=hue)
plt.show()