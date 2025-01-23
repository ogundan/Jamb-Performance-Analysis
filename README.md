# Jamb-Performance-Analysis
A Project for Teachers' benefit at Ijaya 2025 AI and Robotic Training For Students at AIRLAB UNILAG
import pandas as pd
import os
import kagglehub

# Download latest version
path = kagglehub.dataset_download("idowuadamo/students-performance-in-2024-jamb")

print("Path to dataset files:", path)

os.listdir(path)
# read data from path using pandas
df =pd.read_csv(os.path.join(path,'jamb_exam_results.csv'))
df.describe()
df.describe().T
df.head()
df.head(4)
df.tail()
df.tail(4)
df.tail(10)
df.sample()
## Toc heck Random Sample
df.sample(10)
##To check missing value
###isnull is a function
df.isnull()
df.isnull().sum()
###df.info gives me information of the dataset
df.info()
#Day 4
##Asking Our Data Set Questions
###1. Students with maximum Score
df[df['JAMB_Score']== df['JAMB_Score'].max()]
###Parental Education Level on Student performance
  df.shape
  df.dropna()
  1.
  df.columns
  import matplotlib.pyplot as plt
import seaborn as sns


plt.figure(figsize=(10,8))
sns.histplot(data=df['JAMB_Score'])
plt.show()
df.shape
df.dropna(inplace=True)
###Parental Education Level on Students' Performance
import matplotlib.pyplot as plt
import seaborn as sns


plt.figure(figsize=(8,4))
sns.histplot(data=df['JAMB_Score'])
plt.show()
plt.figure(figsize=(8,4))
sns.histplot(data=df,x='JAMB_Score',hue='Parent_Education_Level')
plt.show()
df.dropna(inplace=True)
df['Parent_Education_Level'].unique()
df.shape
###group the parental education by jamb score
df.groupby('Parent_Education_Level')['JAMB_Score'].mean()
    df['Parent_Education_Level'].unique()
    array['Tertiary','primary','secondary'], dtype=object

  print(df['Parent_Education_Level'].unique())

  ## Class Two: Web Applications By Lukman Abdulwahab A.K.A Litmus



  ##Check Python Version
  python -V


  ## Creating Virtual Environment
  


