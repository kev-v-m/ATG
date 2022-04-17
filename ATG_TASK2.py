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
driver = webdriver.Chrome('C:/Users/Kevin/Downloads/chromedriver_win32/chromedriver.exe')
os.chdir('C:\\Users\Kevin\Desktop\ATG')


# In[2]:


driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')


# In[3]:


#selecting username and pass fields

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='password']")))


# In[4]:


#entering username and pass

username.clear()
username.send_keys("enter yuor email")
password.clear()
password.send_keys("enter your pass")


# In[5]:


#clicking on submit
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()


# In[6]:


f = open('JOB_PROFILES.txt', 'r')


# In[7]:


#choosing random states and opening a ext file TASK_2

states=['Maharashtra','Delhi','Kerala','Karnataka','Tamil Nadu']
f = open('TASK_2.txt', 'w')


#going to linked jobs
driver.get('https://www.linkedin.com/jobs/')


# In[11]:


#iterating through states 
    
for i in states:   
    #reading job profile.txt which contains all jobs from question 1 line by line
    with open('JOB_PROFILES.txt') as f:
        line = f.readline()
        
        
        while line:
            #selecting job field in linkedin jobs and entering the job from jobprofiles as line
            jp = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class='jobs-search-box__text-input jobs-search-box__keyboard-text-input']")))
            jp.clear()
            jp.send_keys(line)
            
            #selecting location field in linkedin jobs and entering the location from states
            jl = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class='jobs-search-box__text-input']")))
            jl.clear()
            jl.send_keys(i)
            
            #clicking on search button
            button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='button']" ))).click()
            
            #selecting all elements from the company name and nature of job(remot/onsite/hybrid)
            type_of_job=driver.find_elements_by_class_name("job-card-container__workplace-type")
            company=driver.find_elements_by_class_name("ember-view job-card-container__link job-card-list__title")
            
            

            
            for i in range(len(location)):   
                
                #writing location
                f.write(i)
                
                #writing company name
                a=company[i].text
                a = a.encode('utf-8').decode('ascii', 'ignore')
                
                #writing type_of_job
                b=type_of_job[i].text
                b = b.encode('utf-8').decode('ascii', 'ignore')

                f.write(b)
                f.write(line)
                
                
            
            line = f.readline()

            break
            
            


# In[ ]:


<li class="job-card-container__metadata-item job-card-container__metadata-item--workplace-type">
                On-site
              </li>
        
<li class="job-card-container__metadata-item job-card-container__metadata-item--workplace-type">
                On-site
              </li>
        
<li class="job-card-container__metadata-item job-card-container__metadata-item--workplace-type">
                Hybrid
              </li>
        
<div id="ember250" class="full-width artdeco-entity-lockup__title ember-view">
            <a data-control-id="3w2FG2G+lEurFLUfFbuqUA==" tabindex="0" href="/jobs/collections/recommended/?currentJobId=3024449082&amp;start=0" id="ember251" class="ember-view job-card-container__link job-card-list__title">
              Web Development Intern
            </a>
      
</div>


# In[ ]:


(/*[@id="ember2913"])

