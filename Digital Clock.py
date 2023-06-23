#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import all the required libraries first
import sys
from tkinter import *
#import time library to obtain current time
import time


# In[2]:


#create a function timing and variable current_time
def timing():
    #display current hour,minute,seconds
    current_time = time.strftime("%H : %M : %S")
    #configure the clock
    clock.config(text=current_time)
    #clock will change after every 200 microseconds
    clock.after(200,timing)


# In[3]:


#Create a variable that will store our tkinter window
root=Tk()
#define size of the window
root.geometry("600x300")
#create a variable clock and store label
#First label will show time, second label will show hour:minute:second, third label will show the top digital clock
clock=Label(root,font=("times",60,"bold"),bg="red")
clock.grid(row=2,column=2,pady=25,padx=100)
timing()
 


# In[4]:


#create a variable for digital clock
digital=Label(root,text="Digital Clock",font="times 24 bold")
digital.grid(row=0,column=2)
 
nota=Label(root,text="hours        minutes        seconds",font="times 15 bold")
nota.grid(row=3,column=2)


# In[5]:


root.mainloop()


# In[ ]:




