#!/usr/bin/env python
# coding: utf-8

# In[1]:


import findspark
findspark.init()

import pyspark
from pyspark.sql import SparkSession
import os
os.chdir('/home/paulcrickard')

spark=SparkSession.builder.master("spark://pop-os.localdomain:7077").appName('DataFrame-Kafka').getOrCreate()


# In[5]:


import os
os.chdir('/home/paulcrickard')
df = spark.read.csv('data.csv')
df.show(5)


# In[6]:


df.printSchema()


# In[7]:


df = spark.read.csv('data.csv',header=True,inferSchema=True)
df.show(5)


# In[8]:


df.printSchema()


# In[15]:


df.select('name').show()


# In[28]:


#df.select(df['age']<40).show()
#df.filter(df['age']<40).show()

#df.filter("age<40").select(['name','age','state']).show()
u40=df.filter("age<40").collect()
u40
u40[0]
u40[0].asDict()
u40[0].asDict()['name']


# In[31]:


for x in u40:
    print(x.asDict())
     


# In[9]:


df.createOrReplaceTempView('people')
df_over40=spark.sql("select * from people where age > 40")
df_over40.show()


# In[11]:


df_over40.describe('age').show()


# In[36]:


df.groupBy('state').count().show()


# In[37]:


df.agg({'age':'mean'}).show()


# In[40]:


import pyspark.sql.functions as f


# In[58]:


df.select(f.collect_set(df['state'])).collect()


# In[62]:


df.select(f.countDistinct('state').alias('states')).show()


# In[70]:


df.select(f.md5('street').alias('hash')).collect()


# In[72]:


df.select(f.reverse(df.state).alias('state-reverse')).collect()


# In[75]:


df.select(f.soundex(df.name).alias('soundex')).collect()


# In[76]:


spark.stop()


# In[ ]:




