#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tensorflow import keras


# In[2]:


reconstructed_model = keras.models.load_model("HW-model.h5")


# In[3]:


reconstructed_model.predict([50])


# In[ ]:




