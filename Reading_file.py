#!/usr/bin/env python
# coding: utf-8

# In[7]:


file=open("E:\python_Google\Spider.txt")
print(file.read())
print(file.readlines())
file.close()


# In[9]:


file=open("E:\python_Google\Spider.txt")
print(file.readlines())


# In[10]:


#!/usr/bin/env python3


import shutil
import psutil

def checK_disk_usage(disk):
    du=shutil.disk_usage(disk)
    free=du.free/du.total*100
    return  free > 20
def check_cpu_usage():
    usage=psutil.cpu_precent(1)
    return usage < 75

if not checK_disk_usage("/") or not check_cpu_usage:
    print("Error")
else:
    print("Everthing is OK") 


# In[11]:


with open("E:\python_Google\Spider.txt") as file:
    print(file.read())


# In[24]:


with open("E:\python_Google\Spider.txt","r+") as file:
    print(file.read())
    


# In[23]:


with open("E:\python_Google\Spider.txt","a") as file:
    file.write("Rishiesh")


# In[21]:


with open("E:\python_Google\Spider.txt","w") as file:
    file.write("hello ")
   
    


# In[ ]:




