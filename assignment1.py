#!/usr/bin/env python
# coding: utf-8

# # Assignment 
# 1)write a program to print list of number between 2000 to 3200 which divisible by 7 and not multipled by 5.
# 

# In[35]:


#num%7==0 is for divisible by 7 
#n-5 till zero is for multiple by 5 using while
#printing the line by using end in print function



for i in range(2000,3200): 
    if(i%7==0): 
        j=i
        while(j > 0): j-=5    
        if(j != 0): print (i,end=",")
               
        
        







