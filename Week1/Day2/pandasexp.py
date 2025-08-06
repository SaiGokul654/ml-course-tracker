import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\Geethika Paruchuri\Downloads\annual-enterprise-survey-2024-financial-year-provisional.csv')
print(df)


df.head()

df.tail()

col=df['Year'].describe()
print(col)


df['new']=df['Year']+1
print(df['new'])

df=df.drop(['Year'],axis=1)
df.head()

df.shape


df.count()

df=df.drop_duplicates()
print(df)

df.isnull().sum()


c=df.corr()
print(c)


