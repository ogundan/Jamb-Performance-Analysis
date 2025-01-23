## Importing Of Necessary Libraries

import pandas as pd
import os

import kagglehub
import matplotlib.pyplot as plt
import seaborn as sns

## Reading Data From Kaggle


# Download latest version
path = kagglehub.dataset_download("idowuadamo/students-performance-in-2024-jamb")

print("Path to dataset files:", path)

os.listdir(path)

# read data from path using pandas
df = pd.read_csv(os.path.join(path, 'jamb_exam_results.csv'))

# Questions To Ask The Data

## 1. Student With Maximum Score

df[df['JAMB_Score'] == df['JAMB_Score'].max()]



df['Parent_Education_Level'].unique()

# group the parental education by jamb score average
data_pel = df.groupby('Parent_Education_Level')['JAMB_Score'].mean()

grouped_data = df.groupby('Study_Hours_Per_Week')['JAMB_Score'].mean().reset_index()


