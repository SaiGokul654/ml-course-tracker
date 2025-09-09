#Building the model like pro using sklearn


#load the data
#understand and vizualize the data
#data preparation train-test split,normalization or rescalling
#training the model
#residual analysis on training data
#prediction
#evaluation

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv('student-por.csv')

df.shape

df.head()

df.describe()

df.columns

sns.jointplot(x='school',y='guardian',data=df,kind='scatter')

plt.figure()
sns.heatmap(df.corr(numeric_only=True), annot=True)

x=df[['school']]
y=df[['guardian']]

df.corr(numeric_only=True)

#Datapreparation
from sklearn.model_selection import train_test_split

# Assuming you want to split the dataframe into training and testing sets with a 75/25 ratio
train_df, test_df = train_test_split(df, test_size=0.25)

print("Training set shape:", train_df.shape)
print("Testing set shape:", test_df.shape)



