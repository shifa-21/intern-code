# -*- coding: utf-8 -*-
"""TASK 3_EDA_on_dataset_samplesuperstore.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OQZOx-dMdPIPU5U6M-23mSA2CSnH7xpz

## **SHIFA USSUDOOR**

##SPARK FOUNDATION
Graduate Rotational Internship Program

##Task 2

Perform ‘Exploratory Data Analysis’ on dataset ‘SampleSuperstore’

# IMPORTING LIBRARIES
"""

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""# LOADING THE DATASET"""

file_name = "SampleSuperstore.csv"
df = pd.read_csv(file_name)

df.sample(9)

df.tail()

"""# CHECK THE MISSING VALUE"""

df.isnull().sum()

"""# Finding Total number of null values in a dataset"""

print("total number of null values = ",df.isnull().sum().sum())

"""# Full summary of the dataframe """

print(df.info())

"""# Statistical details of the dataset"""

df.describe()

"""# Shape of dataset"""

df.shape

"""# Find the dtypes in the Dataset"""

df.dtypes

"""# Finding all the column names inside the dataset"""

df.columns

"""# Check the dataset for duplicate and dropping element"""

df.duplicated().sum()

df.drop_duplicates()

"""# Function return Series with number of distinct observations over requested axis"""

df.nunique()

"""# Find the correlation of dataset"""

df.corr()

"""# Find the covariance of dataset"""

df.cov()

"""# Find the Series containing counts of unique values"""

df.value_counts()

"""# Deleting the Variable"""

col=['Postal Code']
df1=df.drop(columns=col,axis=1)

"""# Proper Visualization of the data set"""

plt.figure(figsize=(16,8))
plt.bar('Sub-Category','Category', data=df)
plt.show()

print(df1['State'].value_counts())
plt.figure(figsize=(15,8))
sns.countplot(x=df1['State'])
plt.xticks(rotation=90)
plt.show()

print(df['Sub-Category'].value_counts())
plt.figure(figsize=(12,6))
sns.countplot(x=df['Sub-Category'])
plt.xticks(rotation=90)
plt.show()

"""# HEATMAP OF DATASET"""

fig,axes = plt.subplots(1,1,figsize=(9,6))
sns.heatmap(df.corr(), annot= True)
plt.show()

fig,axes = plt.subplots(1,1,figsize=(9,6))
sns.heatmap(df.cov(), annot= True)
plt.show()

sns.countplot(x=df['Segment'])

sns.countplot(x=df['Region'])

plt.figure(figsize=(40,25))
sns.barplot(x=df['Sub-Category'], y=df['Profit'])

plt.figure(figsize = (10,4))
sns.lineplot('Discount', 'Profit', data = df, color = 'r', label= 'Discount')
plt.legend()

df1.hist(bins=50 ,figsize=(20,15))
plt.show()

figsize=(15,10)
sns.pairplot(df1,hue='Sub-Category')

grouped=pd.DataFrame(df.groupby(['Ship Mode','Segment','Category','Sub-Category','State','Region'])['Quantity','Discount','Sales','Profit'].sum().reset_index())
grouped

"""# sum,mean,min,max,count median,standard deviation,Variance of each states of Profit"""

df.groupby("State").Profit.agg(["sum","mean","min","max","count","median","std","var"])

x = df.iloc[:, [9, 10, 11, 12]].values
from sklearn.cluster import KMeans
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', 
                    max_iter = 300, n_init = 10, random_state = 0).fit(x)
    wcss.append(kmeans.inertia_)

sns.set_style("whitegrid") 
sns.FacetGrid(df, hue ="Sub-Category",height = 6).map(plt.scatter,'Sales','Quantity')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], 
            s = 100, c = 'yellow', label = 'Centroids')

plt.legend()

sns.pairplot(df1)

fig, axes = plt.subplots(figsize = (10 , 10))

sns.boxplot(df['Sales'])

fig, axes = plt.subplots(figsize = (10 , 10))

sns.boxplot(df['Discount'])

fig, axes = plt.subplots(figsize = (10 , 10))

sns.boxplot(df['Profit'])

Q1 = df.quantile(q = 0.25, axis = 0, numeric_only = True, interpolation = 'linear')

Q3 = df.quantile(q = 0.75, axis = 0, numeric_only = True, interpolation = 'linear')

IQR = Q3 - Q1

print(IQR)

df.value_counts().nlargest().plot(kind = 'bar' , figsize = (10 , 5))

"""# SCATTER PLOT"""

fig, ax = plt.subplots(figsize = (10 , 6))
ax.scatter(df["Sales"] , df["Profit"])
ax.set_xlabel('Sales')
ax.set_ylabel('Profit')
plt.show()

"""# Distribution Plot"""

print(df['Sales'].describe())
plt.figure(figsize = (9 , 8))
sns.distplot(df['Sales'], color = 'b', bins = 100, hist_kws = {'alpha': 0.4});