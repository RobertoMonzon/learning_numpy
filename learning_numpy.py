#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np


# In[3]:


matriz_1=np.array([1,2,3,4,5,6,7,8,9])


# In[5]:


print(matriz_1)


# In[7]:


matriz_2=np.array([[12,34,56,78,90],[10,29,38,47,56],[13,25,46,57,80]])


# In[8]:


print(matriz_2)


# In[12]:


lista_3=[1,2,3,4,5]


# In[13]:


matriz_3= np.array(lista_3)


# In[14]:


print(matriz_3)


# In[15]:


matriz_4=np.arange(24).reshape(6,4)


# In[16]:


print(matriz_4)


# In[17]:


print(matriz_4.shape)


# In[19]:


print(matriz_4.ndim)


# In[20]:


print(matriz_4.size)


# In[22]:


matriz_5=np.zeros((3,5))


# In[23]:


print(matriz_5)


# In[24]:


matriz_6=np.arange(10)


# In[25]:


print(matriz_6)


# In[27]:


matriz_7=np.linspace(99,88,25)


# In[28]:


print(matriz_7)


# In[30]:


matriz_8=np.arange(24).reshape(2,3,4)


# In[31]:


print(matriz_8)


# In[32]:


matriz_9 = np.arange(27).reshape(3,9)


# In[34]:


print(matriz_9)


# In[36]:


matriz_10= np.array([99,10,88,20,77,30,66,40,55])


# In[38]:


print(np.sort(matriz_10))


# In[39]:


matriz_11= np.array([2,3])


# In[41]:


print(np.power(matriz_11,3))


# In[42]:


matriz_12= np.array([99,10,88,20,77,30,66,40,55])


# In[44]:


print(np.array(matriz_12>50))


# In[47]:


print(np.array(matriz_12.max()))


# In[48]:


print(np.array(matriz_12.min()))


# In[51]:


matriz_13= np.array([90,11,80,22,70,33,60,44,50])


# In[52]:


print(np.concatenate((matriz_12,matriz_13)))


# In[53]:


m1=np.array([[1,2],[3,4]])


# In[54]:


m2=np.array([[5,6],[7,8]])


# In[55]:


print(m1+m2)


# In[57]:


print(m1.dot(m2))


# In[77]:


m=np.random.randint(10)
print(m)


# In[78]:


m=np.random.randint(10,size=(5))
print(m)


# In[79]:


m=np.random.randint(10,size=(3,3))
print(m)


# In[80]:


m=np.random.rand(5)
print(m)


# In[82]:


m=np.random.rand(2,2)
print(m)


# In[96]:


m=np.random.choice([3,5,9,5,1])
print(m)


# In[95]:


m=np.random.choice([3,5,9,5,1], size=(2,3))
print(m)


# In[130]:


m=np.random.choice([2,4,6],p=[0.5,0.5,0.0],size=[1])
print(m)


# In[142]:


m=np.random.choice([2,4,8,10],p=[0.3,0.5,0.1,0.1],size=[50])
print(m)


# In[144]:


m=np.array([[0,1,2],[4,2,3]])
print(m)
print("\n")
print(np.sum(m,axis=0))


# In[145]:


m=np.array([[0,1,2],[4,2,3]])
print(m)
print("\n")
print(np.sum(m,axis=1))


# In[149]:


m=np.array([[1,1],[1,1]])
n=np.array([[2,2],[2,2]])
print(m)
print("\n")
print(n)
print("\n")
print(np.concatenate([m,n],axis=0))


# In[150]:


m=np.array([[1,1],[1,1]])
n=np.array([[2,2],[2,2]])
print(m)
print("\n")
print(n)
print("\n")
print(np.concatenate([m,n],axis=1))


# In[153]:


m=np.array([1,1])
n=np.array([2,2])
print(m)
print("\n")
print(n)
print("\n")
print(np.concatenate([m,n],axis=0))


# In[159]:


n=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(n)
print("\n")
print(np.amin(n))


# In[158]:


n=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(n)
print("\n")
print(np.amax(n))


# In[160]:


n=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(n)
print("\n")
print(np.amin(n,1))


# In[161]:


n=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(n)
print("\n")
print(np.ptp(n))


# In[162]:


n=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(n)
print("\n")
print(np.ptp(n,axis=1))


# In[163]:


n=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(n)
print("\n")
print(np.percentile(n,50))


# In[164]:


n=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(n)
print("\n")
print(np.percentile(n,50,axis=1))


# In[165]:


n=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(n)
print("\n")
print(np.median(n))


# In[166]:


n=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(n)
print("\n")
print(np.median(n,axis=0))


# In[167]:


n=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(n)
print("\n")
print(np.mean(n))


# In[168]:


n=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(n)
print("\n")
print(np.mean(n,axis=0))


# In[171]:


n=np.array([1,2,3,4,5,6])
print(n)
print("\n")
print(np.average(n))


# In[172]:


n=np.array([1,2,3,4,5,6])
print(n)
print("\n")
print(np.std(n))


# In[177]:


m=np.array([[1,-1,2],[3,2,0]])
print(m)
print("\n")
m1=np.array([[1],[2],[3]])
print(m1)
print("\n")
print(np.transpose(m1))


# In[185]:


ma=np.array([[2,1,-2],[3,0,1],[1,1,-1]])
print(ma)
print("\n")
mb=np.array([[-3],[5],[-2]])
print(mb)
print("\n")
print(np.transpose(mb))
print("\n")
x=np.linalg.solve(ma,mb)
print(x)


# In[188]:


ma=np.array([[2,1,-2],[3,0,1],[1,1,-1]])
print(ma)
print("\n")
mb=np.array([[-3],[5],[-2]])
print(mb)
print("\n")
print(np.transpose(mb))
print("\n")
x=np.linalg.solve(ma,mb)
print(x)
print("\n")
print(np.allclose(np.dot(ma,x),mb))


# In[198]:


m1=np.array([[2,7,3],[2,8,2],[1,3,1]])
print(m1)
print("\n")
m2=np.array([1,1,0])
m2.shape=(3,1)
print(m2)
print("\n")
print(np.linalg.solve(m1,m2))

