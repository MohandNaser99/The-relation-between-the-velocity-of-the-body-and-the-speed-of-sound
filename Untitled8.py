#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


R_u = 8.314
gamma = 1.4 
T_o = 300 
a_o = (R_u *gamma*T_o)**.5
v_max = ((5)**.5)*a_o
print (v_max)


# In[4]:


a= .01
x= .01
a_1 =[0]
v_1 = [v_max]


# In[5]:


while a< a_o :
    a_o1=(a_o)**2
    a_01=(a)**2
    v=(((5*a_o1)-(5*a_01))**.5)
    x = x+.01
    a=x 
    a_1.append(a)
    v_1.append(v)

    


# In[ ]:





# In[6]:


x = np.array(v_1)
y = np.array(a_1)
plt.figure(figsize=(23,10))
plt.plot(x, y,alpha= 1)
plt.xlim([0,140])
plt.ylim([0,60])
plt.title("The relation between the velocity of the body and the speed of sound ")
plt.xlabel("V")
plt.ylabel("a")
plt.show()


# In[ ]:





# In[ ]:




