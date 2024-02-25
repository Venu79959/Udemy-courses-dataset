#!/usr/bin/env python
# coding: utf-8

# # Udemy courses data analysis by KODI VENU

# In[1]:


import pandas as pd
import numpy as np
data = pd.read_csv('udemy_courses.csv')
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt


# In[10]:


data.dtypes


# In[11]:


data = pd.read_csv('udemy_courses.csv',parse_dates=['published_timestamp'])


# In[12]:


data.dtypes


# Displaying Top 10 Rows of the Dataset

# In[13]:


data.head(10)


# Displaying Last 10 Rows of the Dataset

# In[3]:


data.tail(10)


# Finding shape of the Dataset

# In[14]:


data.shape


# In[15]:


print("Number of rows",data.shape[0])
print("Number of columns",data.shape[1])


# Dataset Information

# In[16]:


data.info()


# Checking Null Values in the dataset

# In[17]:


data.isnull().sum()


# In[19]:


sns.heatmap(data.isnull())


# check for duplicate data and drop them

# In[18]:


data.dtypes


# In[20]:


data.duplicated().any()


# In[21]:


dup=data.duplicated().any()
print('Are there any duplicated values in the dataset',dup)


# In[22]:


data=data.drop_duplicates()


# In[23]:


data.duplicated().any()


# Find out number of courses per subjects

# In[24]:


data.columns


# In[25]:


data.head(1)


# In[27]:


data['subject'].value_counts()


# In[30]:


sns.countplot(data['subject'])


# For which levels, udemy courses providing the courses

# In[31]:


data.columns


# In[32]:


data['level'].value_counts()


# In[33]:


sns.countplot(data['level'])


# Display the count of paid and free courses

# In[35]:


data.columns


# In[36]:


data['is_paid'].value_counts()


# In[39]:


sns.countplot(data['is_paid'])
plt.xlabel("is_paid",fontsize=15)
plt.ylabel("Number of free and paid courses",fontsize=15)
plt.xticks(rotation=73)
plt.show()


# Which course has more lectures (free or paid)?

# In[41]:


data.groupby(['is_paid']).mean()


# Which courses have a higher number of subscribers free or paid?

# In[42]:


data.columns


# In[43]:


sns.barplot(x='is_paid',y='num_subscribers',data=data)


# Which level has the highest number of subscribers?

# In[44]:


data.columns


# In[47]:


sns.barplot(x='level',y='num_subscribers',data=data)
plt.show()


# Find most popular course title?

# In[45]:


data.columns


# In[49]:


data['num_subscribers'].max()==data['num_subscribers']


# In[50]:


data[data['num_subscribers'].max()==data['num_subscribers']]


# In[51]:


data[data['num_subscribers'].max()==data['num_subscribers']]['course_title']


# Display 10 most popular courses as per number of subscribers

# In[48]:


data.columns


# In[52]:


data.sort_values(by='num_subscribers',ascending=False)


# In[54]:


top_10=data.sort_values(by='num_subscribers',ascending=False).head(10)


# In[55]:


top_10


# In[56]:


sns.barplot(x='num_subscribers',y='course_title',data=top_10)


# Find the course which is having the highest number of reviews

# In[57]:


data.columns


# In[62]:


plt.figure(figsize=(10,4))
sns.barplot(x='subject',y='num_reviews',data=data)


# Does price affect the number of reviews?

# In[63]:


data.columns


# In[70]:


plt.figure(figsize=(16,6))
sns.scatterplot(x='price',y='num_reviews',data=data)
plt.show()


# Find the total number of courses related to python?

# In[71]:


data.columns


# In[72]:


data['course_title'].str.contains('python',case=False)


# In[73]:


data[data['course_title'].str.contains('python',case=False)]


# In[74]:


len(data[data['course_title'].str.contains('python',case=False)])


# Display 10 most popular python courses as per number of subscribers

# In[75]:


data.columns


# In[76]:


data[data['course_title'].str.contains('python',case=False)]


# In[77]:


data[data['course_title'].str.contains('python',case=False)].sort_values(by='num_subscribers',ascending=False)


# In[79]:


v=data[data['course_title'].str.contains('python',case=False)].sort_values(by='num_subscribers',ascending=False).head(10)


# In[80]:


v


# In[81]:


sns.barplot(x='num_subscribers',y='course_title',data=v)


# In which year the highest number of courses were posted?

# In[82]:


data.columns


# In[84]:


data['Year']=data['published_timestamp'].dt.year


# In[85]:


data.head(1)


# In[86]:


data['Year'].value_counts()


# In[87]:


sns.countplot('Year',data=data)


# Display category-wise count of posted subjects[Year Wise]

# In[88]:


data.columns


# In[89]:


data.groupby('Year')['subject'].value_counts()


# In[ ]:




