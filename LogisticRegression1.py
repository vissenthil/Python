print('Implementing logistic regression')
print('Stages of implementing any algorithem in machinelearning is')
print('1. Collecting data- import libraries that are used for collecting data')
print('2. Analyizing data -Goes to various fileds and anlayising the data')
print('3. Data Wrangling -Cleaning the data- remove the unncessary items ')
print('4. Train & test split -To train our model')
print('5. Accuracy check')
# Collect your data -Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
titanic_data = pd.read_csv('D:\\python\\MLProjects\\Titanic-Dataset.csv')
print(titanic_data.head(10))
print(titanic_data.isnull().sum())
print(titanic_data.describe())
print('No of passengers in the original data',len(titanic_data.index))
print(titanic_data.info)
print('2. Analying data ')
sns.countplot(x='Survived', data=titanic_data)
plt.show()
print('Find out Sexwise Survived Numbers')
sns.countplot(x='Survived', hue='Sex', data=titanic_data)
plt.show()
print('Finout out classwise Survived results')
sns.countplot(x='Survived', hue ='Pclass', data = titanic_data)
plt.show()
print('Histogram plot to know the agewise travers details')
titanic_data['Age'].plot.hist()
plt.show()

titanic_data['Fare'].plot.hist(bins=29,figsize=(10,4))
plt.show()

sns.countplot(x='Survived', hue ='Fare', data = titanic_data)
plt.show()

print('3. Data Wrangling')

print('''Cleaning the data by removing the nan values
        and unncessary columns in the dataset ''')
print(titanic_data.isnull().sum())
sns.heatmap(titanic_data.isnull(),yticklabels=False, cmap='viridis')
#cmap meanis color for the graph
plt.show()

sns.boxplot(x='Pclass', y='Age',data=titanic_data)
plt.show()
print('Cleaning the data')
titanic_data.drop('Cabin',axis=1, inplace=True)
print(titanic_data.isnull().sum())
titanic_data['Age'] = titanic_data['Age'].mean()
print(titanic_data.isnull().sum())
print('Removing null values')
titanic_data.dropna(inplace=True)

sns.heatmap(titanic_data.isnull(), yticklabels=False, cbar=False)
plt.show()
print(''' For logistic regression only accept for numbers(0 and 1) 
          we need to change the string values to 0 or 1 ''')
print(pd.get_dummies(titanic_data['Sex']))
print(''' Here we encoded with 0 or 1 here only one column is enough to
      identify the male or feemale using one column so, we are removind
      Female column here''')
sex = pd.get_dummies(titanic_data['Sex'],drop_first=True)
print('Same we are doing for Embarked columns also')
embarked = pd.get_dummies(titanic_data['Embarked'],drop_first=True)
print('Same we are doing for Pclass columns also')
pcl = pd.get_dummies(titanic_data['Pclass'],drop_first=True)
print('Now concatenate in Our dataset')
titanic_data = pd.concat([titanic_data,sex,embarked,pcl],axis=1)
print(titanic_data.columns)
print('Now drop the unncessary columns in our dataset')
titanic_data.drop(['PassengerId','Ticket','Sex','Embarked','Name','Pclass'],axis=1,inplace=True)
print(titanic_data.info())
print('4.Train and Test split')
print('''Build the model using training data and predict the out put
         using testing data''')
titanic_data.rename(columns = {2:'class2',3:'class3'}, inplace = True)
print(titanic_data.columns)
x = titanic_data.drop('Survived',axis=1) # x is indepentant variable
y = titanic_data['Survived'] # y IS THE TARGET Variable

print(titanic_data.head(19))


from sklearn.model_selection import train_test_split

X_train, X_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=101)
from sklearn.linear_model import LinearRegression
logModel = LinearRegression()
logModel.fit(X_train,y_train)
prediction = logModel.predict(X_test)
prediction = prediction.round()
from sklearn.metrics import classification_report
print(classification_report(y_test,prediction))
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test,prediction)
print('Accuracy of our model is:',accuracy)
print(prediction)
print('SUV Care sales prediction ')
print(''' SUV car company relased a new SUV car in the market. Using previous
         data about SUV Car sales, they want to predict category of peopel 
          who might be intersted in bying this ''')
suv_data = pd.read_csv('D:\\python\\MLProjects\\suv_data.csv')
print(suv_data.head())
suv_data.drop('User ID',axis=1,inplace=True)
gender = pd.get_dummies(suv_data['Gender'],drop_first=True)
print(suv_data.head())
suv_data = pd.concat([suv_data,gender],axis=1)
print(suv_data.head())
suv_data.drop('Gender',axis=1,inplace=True)
print(suv_data.head())
print(suv_data.isnull().sum())
suv_data.drop('Male',axis=1,inplace=True)
x = suv_data.drop('Purchased',axis=1)
y = suv_data['Purchased']
print(x)

from sklearn.linear_model import LinearRegression
SuvModel = LinearRegression()
from sklearn.model_selection import train_test_split

X_Train,X_Test,y_train,y_test =  train_test_split(x,y,test_size=0.2,random_state=1)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_Train = sc.fit_transform(X_Train,)
X_Test  = sc.fit_transform(X_Test)

SuvModel.fit(X_Train,y_train)
SuvPredict = SuvModel.predict(X_Test)
SuvPredict = SuvPredict.round()
'''to avoid this error round is used here: 
ValueError: Classification metrics can't handle a mix of 
binary and continuous targets'''
from  sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test,SuvPredict)
print('Accuracy score of SUV care sales prediction is:',accuracy)


