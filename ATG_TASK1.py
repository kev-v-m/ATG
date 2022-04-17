#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing all necessities

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os


# In[2]:


driver = webdriver.Chrome('C:/Users/Kevin/Downloads/chromedriver_win32/chromedriver.exe')


# In[3]:


os.chdir('C:\\Users\Kevin\Desktop\ATG')


# In[4]:


#finding categories and subcategories

driver.get('https://www.careerguide.com/career-options')
category = driver.find_elements_by_class_name("c-font-bold")
jobs=driver.find_elements_by_class_name("c-content-list-1.c-theme.c-separator-dot")


print(len(jobs),len(category))

#there are more in category than in sub-category as some extra things have been added in the same class. The title is added in the
#same class. The sub category starts from index 1 so we make the adjustment and run a loop only for len(jobs)


# In[5]:


f = open('TASK_1.txt', 'w')

#range is len(jobs) as category has excess in the same class. category begins from index 1. category refers to Aerospace & Aviation/Agriculture
# while jobs is the entire list of all jobs under each category.

#TASK_1 is output for ist question given

for i in range(len(jobs)):    

    f.write(category[i+1].text)
    f.write('\n')
    f.write('\n')
    a=jobs[i].text
    a = a.encode('utf-8').decode('ascii', 'ignore')
    f.write(a)
    f.write('\n')
    f.write('\n')


f.close()

#job_profiles is a file containing all jobs. this is meant to be used for question 2

f = open('JOB_PROFILES.txt', 'w')
for i in range(len(jobs)):    
    a=jobs[i].text
    a = a.encode('utf-8').decode('ascii', 'ignore')
    f.write(a)



f.close()
# In[6]:


print(jobs[1].text)


# In[ ]:




