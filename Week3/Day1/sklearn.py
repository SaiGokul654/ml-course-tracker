import pandas as pd
import numpy as np
df=pd.read_csv('student_scores.csv')
df.head()


df.shape



target=df['Scores']
data=df['Hours']

print(target)
print(data)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(data,target,train_size=0.7,random_state=0)
print(x_train.shape,y_train.shape)
print(x_test.shape,y_test.shape) 


from sklearn.linear_model import LinearRegression
regressor= LinearRegression()
regressor.fit(x_train,y_train)




print('y intercept:',regressor.intercept_)

y_test_pred=regressor.predict(x_test)

temp_df=pd.DataFrame({'Actual':y_test,'Predicted':y_test_pred})
temp_df

import seaborn as sns

sns.histplot(y_test,color='blue',alpha=0.5,bins=5)
sns.histplot(y_test_pred,color='red',alpha=0.5,bins=5)


from sklearn import metrics

print('Root mean sqared error:',np.sqrt(metrics.mean_squared_error(y_test,y_test_pred)))

print (metrics.r2_score(y_test,y_test_pred))