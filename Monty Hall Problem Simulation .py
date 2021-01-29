#!/usr/bin/env python
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt
import random
import seaborn as sns 
sns.set_style('darkgrid')


# In[6]:


# creat the lists for each approach. And set up the options for the doors. 
stay = [ ]
switch = [ ]
doors = ['car', 'goat', 'goat']


# In[7]:


# set up the number of tries to have a representative sample
environment = 10**4

for i in range(environment):
    doors = ['car', 'goat', 'goat']
    #shuffle the doors
    random.shuffle(doors)
    # make the participant chouce random
    contestant_choice = random.choice([0, 1, 2])
    #create the stay results
    stays = doors.pop(contestant_choice)
    doors.remove('goat')
    switches = doors[0]
    stay.append(stays)
    switch.append(switches)
    
    stay_probability = stay.count('car') / int(environment)
    switch_probability = switch.count('car') / int(environment)
    
print('The probability when staying is:', round(stay_probability,4))
print('The probability when switching is:', round(switch_probability,4))

x = ['Stay', 'Switch']
y = [stay_probability,switch_probability]
plt.bar(x, y)
plt.title('Monty Hall Simulation')
plt.xlabel('Decision')
plt.ylabel('Proportion Correct Choice')
plt.show()


# In[ ]:





# ##### Use the previous list and use the following sampling strategies 
# Simple Random Sampling

# In[8]:


#simple random sampling
from random import sample

newStay = sample(stay, 1000)
simple_random_stay_probability = newStay.count('car') / len(newStay)

newSwitch = sample(switch, 1000)
simple_random_switch_probability = newSwitch.count('car') / len(newSwitch)

print('The simple random probability if stay and n=40:', round(simple_random_stay_probability,5))
print('The simple random probability if switch and n=40:', round(simple_random_switch_probability,5))

simple_random_x = ['Stay', 'Switch']
simple_random_y = [simple_random_stay_probability,simple_random_switch_probability]
plt.bar(simple_random_x, simple_random_y)
plt.title('Monty Hall Simple Random Sampling')
plt.xlabel('Decision')
plt.ylabel('Proportion Correct Choice')
plt.show()

