import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt 
category=(['A','B','C','D'])
value=np.random.randint(0,10,size=4)
sns.barplot(x=category,y=value)
plt.show()
