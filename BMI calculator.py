#!/usr/bin/env python
# coding: utf-8

# In[102]:


name1 = "Tú"
weight_kg1 = 74
height_m1 = 1.79


# In[103]:


def BMI(name, weight_kg, height_m):
    bmi = weight_kg / (height_m **2)
    print("BMI của bạn:", bmi)
    if bmi < 25:
        print(name + " không thừa cân")
    else:
        print(name + " thừa cân") 
   


# In[104]:


BMI(name1, weight_kg1, height_m1)


# In[ ]:




