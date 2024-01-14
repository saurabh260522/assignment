#!/usr/bin/env python
# coding: utf-8

# In[1]:


d={}
type(d)


# In[2]:


d1={'key':'saurabh'}
print(d1)


# In[3]:


d2={'name':'saurabh','email':'ingle123@gmail.com','mumber':8600303372}
print(d2)


# In[7]:


d3={123:"saurabh",'_si':'saur',True:123456}


# In[8]:


d3[123]


# In[10]:


d3[True]


# In[11]:


d3[1]


# In[12]:


d4={'name':"sau",'mail_id':'ingle123@gmail.com','name':"saurabh"}


# In[14]:


d4['name']


# In[18]:


d5={'company':'pwskills','course':['web dev','data science','java with das system design']}


# In[19]:


d5


# In[20]:


d5['course'][2]


# In[26]:


d6={'number':[12,3,4,56,7,55],'assignment':(12,4,6,8,545,4),'launch_date':{28,12,14},'class time':{'web dev':8,'data science master':8,'java with das and system desin':7}}


# In[27]:


d6


# In[30]:


d6['class time']['java with das and system desin']


# In[32]:


d6['mentor']=['sudhanshu','krish','anurag','hayder']


# In[33]:


d6


# In[35]:


del d6['number']


# In[36]:


d6


# In[38]:


d6.keys()


# In[40]:


d6.values()


# In[42]:


d6.items()


# In[43]:


list(d6.items())


# In[44]:


d6['number']=[1,2,3,4,5,6]


# In[45]:


d6


# In[46]:


l1=['saurabh','prasheek','raj','rohit']


# In[47]:


l1.insert(1,'brother')


# In[48]:


l1


# In[49]:


del d6['number']


# In[50]:


d6


# In[51]:


d6.pop('assignment')


# In[52]:


d6


# In[53]:


d6.pop()


# # control statement

# if , elif , else 

# In[83]:


marks = int(input("enter your maarks"))
if marks >= 80 :
    print('you will be the part of A0 batch')
elif marks >= 60 and marks <80:
    print('you will be the part of A1 baytch')
elif marks >= 40 and marks < 60:
    print('print you will be the part of A2 batch')
else :
    print('you will be the part of A3 batch ')


# In[59]:


10>=80


# In[76]:


marks = int(input("enter your maarks"))


# In[77]:


marks


# In[78]:


type(marks)


# In[88]:


price = int(input("enter price"))
if price > 1000 :
    print('i will not purchase')
else :
    print('i will purchase')


# In[97]:


price = int(input("enter price"))
if price > 1000 :
    print('i will not purchase')
    if price >5000:
        print("this is too much")
    elif price <2000:
        print("it's ok")
elif price <1000 :
    print("i will purchase")
    print('i will not purchase')
    if price >5000:
        print("this is too much")
    elif price <2000:
        print("it's ok")
else:
    print("not intrested")


# # LOOP

# In[102]:


l=[1,2,3,4,5,6,7,8]


# In[103]:


print(l)


# In[104]:


l[0]+1


# In[106]:


l1=[]


# In[108]:


l1.append(l[0]+1)


# In[109]:


l1


# In[110]:


l


# for loop

# In[117]:


l1=[]
for i in l:
    print(i+1)
    l1.append(i+1)
l1


# In[118]:


l=["saurabh","ingle","pwskills","courses"]


# In[120]:


l1=[]
for i in l :
    print(i)
    l1.append(i.upper())


# In[121]:


l1


# In[122]:


l=[1,2,3,4,4,"sau","rohit",123,45.52,"abc"]


# In[124]:


l1_num=[]
l2_str=[]
for i in l :
    if type(i)== int or type(i)== float:
        l1_num.append(i)
    else :
        l2_str.append(i)


# In[125]:


l1_num


# In[126]:


l2_str


# In[ ]:




