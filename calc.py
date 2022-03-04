#!/usr/bin/env python
# coding: utf-8

# In[15]:


def fact(x):
    if x==1:
        return x
    else:
        return (x*fact(x-1))


# In[16]:


fact(5)


# In[13]:


def temp_conversion(temp):
    return (temp*9/5)+32


# In[14]:


temp_conversion(5)


# In[ ]:




