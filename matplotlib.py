#!/usr/bin/env python
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt


# In[6]:


#from matplotlib import pyplot as plt


# In[7]:


x=[1,2,3,4,5,6]
y=[3,4,5,6,7,8]


# In[8]:


plt.bar(x,y)
plt.show


# In[9]:


plt.plot(x,y)
plt.show


# In[10]:


plt.barh(x,y)
plt.show


# In[11]:


plt.scatter(x,y)
plt.show()


# In[12]:


x=[102,104,105,103,108]
#x=[1,2,3,4,5]
#y=[3,4,5,2,1]
y=[45,67,55,23,77]


# In[13]:


plt.title("sample bar graph")
plt.xlabel("students region")
plt.ylabel("marks")
plt.bar(x,y,color='red')
#plt.bar(x,y)
plt.show


# In[17]:


x=[1,2,3,4,5,6]
y=[3,4,5,6,7,3]


# In[18]:


barplot = plt.bar(x,y)
for bar in barplot:
    yval=bar.get_height()
    plt.text(bar.get_x()+bar.get_width()/2.0,yval,int(yval),va="bottom")
    #plt.text(bar.get_x()+bar.get_width()/2.0,yval,int(yval),va="top")
plt.title("sample bar graph")
plt.xlabel("students")
plt.ylabel("marks")
plt.show()


# In[16]:


#13-06-2022


# In[10]:


import matplotlib.pyplot as plt


# In[23]:


x=[1,2,3,4,5,6,7]
y=[34,56,67,89,66,54,55]
plt.bar(x,y)
plt.title("sample bar graph")
plt.xlabel("students")
plt.ylabel("marks")
#plt.yticks([59,37,93,68,33,44,99])
plt.yticks([ 10,20,30,40,50,60,70,80,90,100])
#plt.xticks([2,3,4,5,1,5,6])
plt.show


# In[27]:


x=["cat","dog","bull","fox","rat"]
y=["wild","pet","mamel","cruel","insect"]
#x=[1,2,3,4,5]
#y=[3,5,6,8,9]
plt.bar(x,y)
plt.title("sample bar graph")
plt.xlabel("animals")
plt.ylabel("nature")
plt.bar(x,y,color="red")
plt.show()


# In[28]:


#sorting


# In[29]:


x=["g","t","y","u","e"]
y=[4,7,9,3,6]
# sort the data based on y value
y,x = zip(*sorted(zip(y,x)))# sorted order
plt.bar(x,y,color="red",label="sorted data")
plt.legend()
plt.title("sample bar graph")
plt.xlabel("marks")
plt.ylabel("students")
plt.show()


# In[31]:


x=["g","t","y","u","e"]
y=[4,7,9,3,6]
# sort the data based on y value
x,y = zip(*sorted(zip(x,y)))# sorted order
plt.bar(x,y,color="red",label="sorted data")
plt.legend()
plt.title("sample bar graph")
plt.xlabel("marks")
plt.ylabel("students")
plt.yticks([1,2,3,4,5,6,7,8])
plt.show()


# In[3]:


import pandas as pd


# In[4]:


import numpy as np


# In[5]:


df=pd.DataFrame({"year":[2014,2015,2016,2017,2018],
                "sales":[2000,2300,2600,2700,3000]})


# In[11]:


df.plot("year","sales",kind="line",label="sales per year",color="red")
#df.plot("year","sales",kind="bar",label="sales per year",color="red")
plt.title("line plot")
plt.xlabel("year")
plt.ylabel("sales")
plt.show()


# In[ ]:


#14-06-2022


# In[12]:


df=pd.DataFrame({"year":[2014,2015,2016,2017,2018],
                "sales":[2000,2300,2600,2700,3000]})


# In[13]:


df.plot("year","sales",kind="line",title="simple line plot",label="sales per year",style="r-o")
#df.plot("year","sales",kind="line",title="simple line plot",label="sales per year",style="r-.+")
#df.plot("year","sales",kind="line",title="simple line plot",label="sales per year",style="r--*")
plt.xlabel("year")
plt.ylabel("sales")
plt.show()


# In[14]:


#multi line plot for two lines


# In[17]:


product=pd.DataFrame({"Year":[2014,2015,2016,2017,2018],
                     "productAsales":[2000,2300,2500,2800,3000],
                     "productBsales":[2350,2550,2650,2770,2900]})


# In[19]:


ax=product.plot("Year","productAsales",kind="line",label="product A sales",style="r-*")
product.plot("Year","productBsales",ax=ax,kind="line",label="product B sales",style="b--o")
plt.xlabel("Year")
plt.ylabel("productAsales")
plt.ylabel("productBsales")
plt.show()


# In[20]:


#multiline  plot for three lines


# In[21]:


product=pd.DataFrame({"year":[2013,2014,2015,2016,2017],
                     "productAsales":[2000,2300,2400,2500,2600],
                     "productBsales":[2100,2200,2450,2650,2900],
                      "productBcsales":[2150,2250,2490,2687,2950]})


# In[22]:


x=product.iloc[ : ,0]
a=product.iloc[ : ,1]
b=product.iloc[ : ,2]
c=product.iloc[ : ,3]
plt.plot(x,a,"-0",label="product A sales")
plt.plot(x,b,"--+",label="product B sales")
plt.plot(x,c,"-.",label="product C sales")
plt.legend()
plt.show()


# In[23]:


#pi plot


# In[25]:


import numpy as np
import matplotlib.pyplot as plt


# In[28]:


mobilemarket=["samsung","apple","nokia","moto","honor"]
sales=[200,150,100,250,210]
colors=['r','b','g','y','k']
explode=[0,0,0,0,0.25]
#plt.pi(sales,labels=mobilemarket,autopct='%.2f')
plt.pie(sales,labels=mobilemarket,colors=colors,startangle=30,shadow=True,explode=explode,autopct='%.1f')
plt.title("mobilemarket")
plt.show()


# In[2]:


#15-06-2022


# In[3]:


#histogram


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


#creating random data import numpy as np np.random.seed(1)
mydf=pd.DataFrame({"Age":np.random.randint(low=20,high=80,size=20)})
print(mydf)
#
mydf.plot(bins=6,kind="hist",rwidth=0.98,title="Distribution_Age")
plt.xlabel("bins")
plt.show()


# In[6]:


#Example:
#direct student marks
#covid-19 victims by age
#xlabel_age
#ylabel_frequency
#legend -covid-19 victims by age


# In[7]:


#sub plot
finaldf=pd.DataFrame({"cities":["delhi","chennai","hyderabad","goa"],
                     "2017_Rainfall":[45,65,55,67],
                     "2018_Rainfall":[55,78,67,89]})


# In[8]:


fig=plt.figure()
ax1=fig.add_subplot(121)#1row,2columns,1st table
finaldf.plot("cities","2017_Rainfall",ax=ax1,kind="bar",title="2017 Rainfall")

ax2=fig.add_subplot(122)#1row,2columns,2st table
finaldf.plot("cities","2018_Rainfall",ax=ax2,kind="bar",title="2018 Rainfall")
plt.show()


# In[9]:


finaldf=pd.DataFrame({"cities":["delhi","chennai","hyderabad","goa"],
                     "2017_Rainfall":[45,65,55,67],
                     "2018_Rainfall":[55,78,67,89],
                     "2019_Rainfall":[78,89,90,67]})


# In[10]:


fig=plt.figure()
ax1=fig.add_subplot(131)#1row,2columns,1st table
finaldf.plot("cities","2017_Rainfall",ax=ax1,kind="bar",title="2017 Rainfall")

ax2=fig.add_subplot(132)#1row,2columns,2st table
finaldf.plot("cities","2018_Rainfall",ax=ax2,kind="bar",title="2018 Rainfall")
 

ax3=fig.add_subplot(133)#1row,2columns,3st table
finaldf.plot("cities","2019_Rainfall",ax=ax3,kind="bar",title="2019 Rainfall")
plt.show()
 


# In[12]:


#multi bar chat
company=["infy","google","intel","solvit"]
revenue=[123,134,145,167]
profit=[34,45,65,87]
xpos=np.arange(len(company))
print(xpos)


# In[13]:


plt.bar(xpos,revenue,width=0.4,label="revenue")
plt.bar(xpos+0.4,profit,width=0.4,label="profit")
plt.title("revenue/profi bar chart")
plt.xlabel("company")
plt.xticks(xpos,company)
plt.ylabel("revenue")
plt.legend()
plt.show()


# In[14]:


#with the data set

df=pd.read_csv('crops.csv')
print(df)


# In[16]:


plt.scatter(df.area,df.msp,label="msp")
plt.scatter(df.area,df.yields,label="yields")
#plt.plot(df.area,df.msp,'r-.',label="masp")
#plt.plot(df.area,df.yields,'b-.',label="yields")
plt.legend()
plt.xlabel("area")
plt.show()


# In[ ]:




