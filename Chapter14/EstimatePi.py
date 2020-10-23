#!/usr/bin/env python
# coding: utf-8

# In[23]:


import findspark
findspark.init()


# In[26]:


import pyspark
from pyspark.sql import SparkSession
spark=SparkSession.builder.master("spark://pop-os.localdomain:7077").appName('Pi-Estimation').getOrCreate()


# In[21]:


import random
NUM_SAMPLES=1

def inside(p):
    x, y = random.random(), random.random()
    return x*x + y*y < 1

count = spark.sparkContext('Pi-Example').parallelize(range(0,NUM_SAMPLES)).filter(inside).count()
print("Pi is roughly {}".format(4.0 * count / NUM_SAMPLES))


# In[27]:


spark.stop()


# In[ ]:




