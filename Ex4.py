#!/usr/bin/env python
# coding: utf-8

# Things get more interesting with lists. You'll apply your new knowledge to solve the questions below. Remember to run the following cell first.

# In[3]:


# SETUP - Refer to Ex 1
from learntools.core import binder; binder.bind(globals())
from learntools.python.ex4 import *
print('Setup complete.')


# # 1.
# 
# Complete the function below according to its docstring.

# In[9]:


def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    if len(L)<2:
        return None
    else:
        return L[1]
    pass

# Check your answer
q1.check()


# In[5]:


#q1.hint()
#q1.solution()


# # 2.
# 
# You are analyzing sports teams.  Members of each team are stored in a list. The Coach is the first name in the list, the captain is the second name in the list, and other players are listed after that. 
# These lists are stored in another list, which starts with the best team and proceeds through the list to the worst team last.  Complete the function below to select the **captain** of the worst team.

# In[11]:


def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    return teams[-1][1]
    pass

# Check your answer
q2.check()


# In[10]:


#q2.hint()
#q2.solution()


# # 3.
# 
# The next iteration of Mario Kart will feature an extra-infuriating new item, the *Purple Shell*. When used, it warps the last place racer into first place and the first place racer into last place. Complete the function below to implement the Purple Shell's effect.

# In[22]:


def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    temp = racers[0]
    racers[0] = racers[-1]
    racers[-1] = temp
    pass

# Check your answer
q3.check()


# In[21]:


#q3.hint()
#q3.solution()


# # 4.
# 
# What are the lengths of the following lists? Fill in the variable `lengths` with your predictions. (Try to make a prediction for each list *without* just calling `len()` on it.)

# In[33]:


a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]

# Put your predictions in the list below. Lengths should contain 4 numbers, the
# first being the length of a, the second being the length of b and so on.
lengths = [3,2,0,2]

# Check your answer
q4.check()


# In[32]:


# line below provides some explanation
#q4.solution()


# # 5. <span title="A bit spicy" style="color: darkgreen ">🌶️</span>
# 
# We're using lists to record people who attended our party and what order they arrived in. For example, the following list represents a party with 7 guests, in which Adela showed up first and Ford was the last to arrive:
# 
#     party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
# 
# A guest is considered 'fashionably late' if they arrived after at least half of the party's guests. However, they must not be the very last guest (that's taking it too far). In the above example, Mona and Gilbert are the only guests who were fashionably late.
# 
# Complete the function below which takes a list of party attendees as well as a person, and tells us whether that person is fashionably late.

# In[5]:


def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    order = arrivals.index(name)
    return order >= len(arrivals) / 2 and order != len(arrivals) - 1

    pass

# Check your answer
q5.check()


# In[6]:


#q5.hint()
#q5.solution()


# In[ ]:




