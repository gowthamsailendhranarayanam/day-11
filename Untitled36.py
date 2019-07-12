#!/usr/bin/env python
# coding: utf-8

# In[1]:


def appendData(filename):
    f = open(filename,'a')
    f.write("new Line 1 \n" % i)
    f.write("new Line 2 \n" % i)
    print("file created and succesfully data written")
    return
appendData("file2.txt")
    


# In[ ]:





# In[19]:


def createfile(filename):
    f = open(filename,'w')
    for i in range(10):
        f.write('this is %d line \n' % i)
    print("file is created and data has written")
    return
createfile('file2.txt')


# In[ ]:


#data analysis
def worfcount(filename,word):
    with open(filename,'r') as f:
        if f.mode = 'r':
            x=f.read()
            li = x.split()
        cnt = li.count(word)  
    return
filename = input('enter the file name : ')
word = input('enter the word :')
wordcount()


# In[22]:


def charcount(filename):
    with open(filename,'r') as f:
        if f.mode == 'r':
            x =f.read()
            li = list(x)
    return len(li)
filename = input('enter the filename : ')
charcount(filename)


# In[23]:


fname = input("Enter file name: ") num_lines = 0 with open(fname, 'r') as f: for line in f: num_lines += 1 print("Number of lines:") print(num_lines)
fname = input("Enter file name: ")
num_lines = 0
with open(fname, 'r') as f:
  for line in f:
      num_lines += 1
print("Number of lines:")
print(num_lines)


# In[24]:


def countOfLines(filename):
   with open(filename,'r') as f:
       if f.mode=='r':
           x=f.read()
           li=x.split("\n")
   return len(li)
filename=input('Enter the filename : ')
countOfLines(filename)


# In[26]:


# Function to print the Upper and Lower characters
def caseCount(filename):
   cntUpper=0
   cntLower=0
   with open(filename,'r') as f:
       if f.mode == 'r':
           x=f.read()
           li=list(x)
   for i in li:
       if i.isupper():
           cntUpper += 1 #cntUpper = cntUpper + 1
       elif i.islower():
           cntLower += 1 #cntLower + 1
           output = 'Upper Case = {0} , Lower Case = {1}'.format(cntUpper,cntLower)
   return output
filename = input('Enter the filename : ')
caseCount(filename)


# In[27]:


#os package it contains the certain method which works with os
ls


# In[28]:


ls


# In[30]:


cd Desktop/pythonprog/Git


# In[31]:


li = os.scandir('Git/')
for i in li:
    print(i)


# In[33]:


# Function to print the Upper and Lower characters
def caseCount(filename):
   cntUpper=0
   cntLower=0
   with open(filename,'r') as f:
       if f.mode == 'r':
           x=f.read()
           li=list(x)
   for i in li:
       if i.isupper():
           cntUpper += 1 #cntUpper = cntUpper + 1
       elif i.islower():
           cntLower += 1 #cntLower + 1
            output = 'Upper Case = {0} , Lower Case = {1}'.format(cntUpper,cntLower)
   return output
filename = input('Enter the filename : ')
caseCount(filename)


# In[4]:


# the function of last two digits numbers
import re
def twoDigitMatching(n):
    pattern = '^[0-9]{2}$'
    n = str(n)

    if re.match(pattern,n):
        return True
    return False
print(twoDigitMatching(12))
print(twoDigitMatching(123))


# In[5]:


#to test the user name having 8 characters
def testUsername(s):
    pattern = '^[a-zA-Z]{8}$'
    if re.match(pattern,s):
        return True
    return False
print(testUsername('GitamHYD'))
print(testUsername('Gitam188'))
        


# In[13]:


def emailid(email):
    pattern = '^[0-9a-z][0-9a-z_.]{5,14}[@][a-z0-9]{3,28}[.][a-z]{2,4}$'
    if re.match(pattern,email):
        return True 
    return False
print(emailid('gitam3002@gmail.com'))
print(emailid('gowthamsailendhra3002@gmail.com'))


# In[ ]:


#step 1: make all the turtle package to be imported
import turtle as tt
a1 = tt.Turtle()
tt.backward(100)
tt.done()


# In[ ]:





# In[ ]:


turtle.forward(250)
turtle.done()


# In[ ]:


#step 1: make all the turtle package to be imported
import turtle as tt
a1 = tt.Turtle()
tt.backward(100)
tt.done()


# In[ ]:


# draw square
import turtle as t
a1 =tt.Turtle()
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
a1.forward(150)
a1.right(90)
tt.done()


# In[ ]:




