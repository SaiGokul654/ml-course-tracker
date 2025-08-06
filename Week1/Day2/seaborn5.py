import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt  
x=np.linspace(0,10,100)
y=np.sin(x)
sns.lineplot(x=x,y=y)
plt.title('sine wave')
plt.show()