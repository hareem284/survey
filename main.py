#importing matplotlib
import matplotlib.pyplot as plt
#importing pandas
import pandas as pd
#importing seaborn
import seaborn as sns
#reading csv
df=pd.read_csv("gap.csv")
print(df.head())
df.isnull().any()
#creating countplot on continent
sns.set_style('whitegrid')
sns.set_context('talk')
sns.countplot(df,x='continent',palette='winter',color='aqua')
plt.show()