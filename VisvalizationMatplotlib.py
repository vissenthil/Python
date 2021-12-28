import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x_i = np.linspace(0,5,10)
print(x_i)
y_i = x_i **2
print(y_i)
plt.plot(x_i,y_i)
plt.title('Days Squared Chart')
plt.xlabel('Days')
plt.ylabel('Days squre')
plt.show()
#creating multiplot example
plt.subplot(1,2,1)
plt.plot(x_i,y_i,'r')
plt.subplot(1,2,2)
plt.plot(x_i,y_i,'b')
plt.show()
print('Using figure Objects example')
fig_1 = plt.figure(figsize=[5,4],dpi=100)
axes_1 = fig_1.add_axes([0.1,0.1,0.9,0.9])
axes_1.set_xlabel('Dayd')
axes_1.set_ylabel('Days Squared')
axes_1.set_title('Days Squared Charts')
axes_1.plot(x_i,y_i,label='x/x2')
axes_1.plot(y_i,x_i,label='x2/x')
print('Creates a figure inside a figure')
axes_2 = fig_1.add_axes([0.45,0.45,0.4,0.3])
axes_2.set_xlabel('Dayd')
axes_2.set_ylabel('Days Squared')
axes_2.set_title('Days Squared Charts')
axes_2.plot(x_i,y_i,'r')
axes_2.text(0,40,'Message')
axes_2.legend(loc=1)
plt.show()
print('creating Subplots ')
fig_2, axes_2 = plt.subplots(figsize=(8,4),nrows=1,ncols=3)
plt.tight_layout()
axes_2[1].set_title('Plot 2')
axes_2[1].set_xlabel('X')
axes_2[1].set_ylabel('X Squred')
axes_2[1].plot(x_i,y_i)
plt.show()
print(''' Appearance Optons:

Default colors(b: blue, g: green, r: red, c:cyan, m: magenta,
               y: yellow, k: black, w: white)

color ="0.75" creates a 75% gray
you can use hexcodes color ="#eeefff" 
you can use color names found next like this color="burlywood"
#https://en.wikipedia.org/wiki/web_colors ''')

fig_3 = plt.figure(figsize=(6,4))
axes_3 = fig_3.add_axes([0,0,1,1])
axes_3.plot(x_i,y_i,color='navy',alpha=.75, lw=2, ls='-.',marker='o',markersize=7,markerfacecolor='y',
            markeredgecolor='y',markeredgewidth=4)
plt.show()
print('Setting x axes and y axes limits')
fig_3 = plt.figure(figsize=(6,4))
axes_3 = fig_3.add_axes([0,0,1,1])
axes_3.plot(x_i,y_i,color='navy',alpha=.75, lw=2, ls='-.',marker='o',markersize=7,markerfacecolor='y',
            markeredgecolor='y',markeredgewidth=4)
axes_3.set_xlim([0,3])
axes_3.set_xlim([0,8])
axes_3.grid(True,color="0.6", dashes=(5,2,1,2))
axes_3.set_facecolor('#FACEDE')  # fill color
plt.show()
print('Save a figure to the file name')
fig_3.savefig('C:/Users/viss/OneDrive/Desktop/python/3d_plot.png')
print('Using pandas to plot chart')
ice_df = pd.read_csv('C:/Users/viss/OneDrive/Desktop/python/Files/icecreamsales_csv.csv')
ice_df = ice_df.sort_values('Temperature')
print(ice_df.head())
np_arr = ice_df.values
x2_1 = np_arr[:,0] # to get the first column value
y2_1 = np_arr[:,1] # to get the second column value