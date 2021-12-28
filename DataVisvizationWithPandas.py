import  numpy as np
import  pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from flask import  Flask


df = pd.DataFrame(np.random.randn(10,4), index=pd.date_range('1/1/2000',periods=10),columns=list('ÁBCD'))
print(df.head())
df.plot()
plt.show()
df['Á'].plot()
plt.show()
print('Drawing a bar chart')
df = pd.DataFrame(np.random.rand(10,4),columns=['A','B','C','D'])
df.plot.bar()
plt.show()
print('Creating bar chart for only on column')
df['A'].plot.bar()
plt.show()
print('Create bar chart in harisandel ')
df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
df.plot.barh(stacked=True)
plt.show()
print('Creating Histogram chart')
df = pd.DataFrame({'a':np.random.randn(1000)+1 ,'b':np.random.randn(1000),'c':np.random.randn(1000)-1},
                  columns=['a','b','c'])
df.plot.hist(bins=30)
plt.show()
df['b'].plot.hist(bins=6)
plt.show()

df = pd.DataFrame(np.random.rand(10,5),columns=['A','B', 'C','D','E'])
df.plot.box()
plt.show()

df = pd.DataFrame(np.random.rand(10,5),columns=['a','b','c','d','e'])
df.plot.area()
plt.show()
df['e'].plot.area()
plt.show()
df = pd.DataFrame(np.random.rand(50,5),columns=['a','b','c','d','e'])
df.plot.scatter(x = 'a',y = 'b')
plt.show()

df = pd.DataFrame(3 * np.random.rand(5),index=['a','b','c','d','e'], columns=['x'])
df.plot.pie(subplots=True)
plt.show()

x = np.linspace(0,10,100)
y = 4 + 2 * np.sin(2 * x)
print(y)
fig,ax = plt.subplots()
ax.plot(x,y,linewidth=2.0)
ax.set(xlim=(0,8), xticks=np.arange(1,8),
       ylim=(0,8), yticks=np.arange(1,8))
plt.show()
fig = plt.figure('[10,10]')
ax = fig.add_axes([0,0,1,1])
lang = ['python','java','c','c++']
stud = [50,40,30,20]
ax.bar(lang,stud)
plt.show()
fig,ax = plt.subplots(1,1)
a = np.array([23,45,67,12,67,85,200,34,98,69,235,62,85])
ax.hist(a,bins = [0,23,56,79,100])
ax.set_title('Histogram of results')
ax.set_xticks([0,23,56,79,100])
ax.set_xlabel('Marks')
ax.set_ylabel('No of students')
plt.show()

import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", title="A Plotly Express Figure")

# If you print the figure, you'll see that it's just a regular figure with data and layout
# print(fig)

fig.show()