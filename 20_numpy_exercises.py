#!/usr/bin/env python
# coding: utf-8

# # 20 numpy exercises

# This is a collection of exercises that have been collected in the numpy mailing list, on stack overflow and in the numpy documentation. The goal of this collection is to offer a quick reference for both old and new users but also to provide a set of exercises for those who teach.

# ### 1. Import the numpy package under the name np (★☆☆)

# In[8]:


import numpy as np


# ### 2. Print the numpy version and the configuration (★☆☆)

# In[24]:


print(np.version.version)
print("\n")


# In[25]:


print(np.show_config())
print("\n")


# ### 3. Create a null vector of size 10 (★☆☆)

# In[14]:


vector_10=np.zeros(10)
print(vector_10)


# ### 4. How to find the memory size of any array (★☆☆)

# In[18]:


memory_array=np.array([1,2,3,4,5,6])
print((memory_array.itemsize)*(memory_array.size))


# ### 5. How to get the documentation of the numpy add function from the command line? (★☆☆)

# In[27]:


print(np.info(np.add))
print("\n")


# ### 6. Create a null vector of size 10 but the fifth value which is 1 (★☆☆)

# In[31]:


vector_10_null=np.zeros(10)
print(vector_10_null)
print("\n")
vector_10_null[4]=1
print(vector_10_null)
print("\n")


# ### 7. Create a vector with values ranging from 10 to 49 (★☆☆)

# In[36]:


vector_10_49=np.arange(10,50)
print(vector_10_49)


# ### 8. Reverse a vector (first element becomes last) (★☆☆)

# In[40]:


flip_array=np.array([1,2,3,4,5,6])
print(flip_array)
print("\n")
flipped_array=np.flip(flip_array)
print(flipped_array)
print("\n")


# ### 9. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)

# In[9]:


array=np.arange(9).reshape(3,3)
print(array)


# ### 10. Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)

# In[11]:


arr=np.nonzero([[1,2,0,0,4,0]])
print(arr)


# ### 11. Create a 3x3 identity matrix (★☆☆)

# In[12]:


arr=np.identity(3)
print(arr)


# ### 12. Create a 3x3x3 array with random values (★☆☆)

# In[13]:


random_arr=np.random.rand(3,3)
print(random_arr)


# ### 13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)

# In[17]:


random_arr=np.random.rand(10,10)
print(random_arr)
print("\n")
print(random_arr.max())
print("\n")
print(random_arr.min())


# ### 14. Create a random vector of size 30 and find the mean value (★☆☆)

# In[18]:


random_arr=np.random.rand(30,30)
print(random_arr)
print("\n")
print(random_arr.mean())
print("\n")


# ### 15. Create a 2d array with 1 on the border and 0 inside (★☆☆)

# In[25]:


array_center=np.zeros([3,3])
array_center[1,1]=1
print(array_center)


# ### 16. How to add a border (filled with 0's) around an existing array? (★☆☆)

# In[32]:


array_border=np.arange(1,10).reshape(3,3)
print(array_border)
array_border = np.pad(array_border, pad_width=1, mode='constant', constant_values=0)
print("\n")
print(array_border)


# ### 17. What is the result of the following expression? (★☆☆)

# In[33]:


# 0 * np.nan
# np.nan == np.nan
# np.inf > np.nan
# np.nan - np.nan
# np.nan in set([np.nan])
# 0.3 == 3 * 0.1


# In[35]:


print(0 * np.nan)
print(np.nan == np.nan) 
print(np.inf > np.nan) 
print(np.nan - np.nan) 
print(np.nan in set([np.nan])) 
print( 0.3 == 3 * 0.1)


# ### 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)

# In[42]:


diag = np.diag(1+np.arange(4),k=-1)
print(diag)


# ### 19. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)

# In[58]:


checkboard = np.zeros((8,8),dtype=int)
checkboard[1::2, ::2] = 1
checkboard[::2, 1::2] = 1

print(checkboard)


# ### 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element? (★☆☆)

# In[59]:


print(np.unravel_index(99,(6,7,8)))

