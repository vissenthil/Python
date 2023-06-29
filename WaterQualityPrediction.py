# https://www.youtube.com/watch?v=MWLUtTlHxpw
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
data = pd.read_csv('D:\\python\\MLProjects\\MLForCloudDeployment_Heroku\\SourceFiles\\water_potability.csv')
print(data.shape) # row, columns
print(data.describe())
print(data.info())
print(data.columns)
print(data.isnull().sum())
print('Data cleaning ')
data.fillna(data.mean(),inplace=True)
print(data.isnull().sum())
print('EDA - Exploratory data analysis')
print(data.describe())
print('Checking the co-relation ')
sns.heatmap(data.corr(),annot=True, cmap='terrain')
plt.show()
print('Let check with box plot to see any outlayers in our data')
plt.boxplot(data)
plt.show()
data.boxplot()
plt.show()
print('Checking how many target values count present')
print(data['Potability'].value_counts())
sns.countplot(data['Potability'])
plt.show()
print('To check the nomality normally distributed or not')
data.hist(figsize=(15,14))
plt.show()
#sns.barplot(x=data['ph'],y=data['Hardness'],hue=data['Potability'])
#plt.show()
sns.scatterplot(x=data['ph'],y=data['Potability'])
plt.show()

print('Now model training and model optimization')
x = data.drop('Potability',axis=1)
y = data['Potability']
np.round(y)

print(x.shape)
from sklearn.svm import SVR,SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=131)

print('Using Support vector Regression Method')
model = SVR(kernel='rbf',gamma=15,C=10)
model.fit(x_train,y_train)
y_predict = model.predict(x_test)
y_predict = np.round(y_predict)
y_test = np.round(y_test)
print('Model accuracy of rbf kernal is ',accuracy_score(y_test,y_predict))

model = SVR(kernel='poly',degree=5)
model.fit(x_train,y_train)
y_predict = model.predict(x_test)
y_predict = np.round(y_predict)
y_test = np.round(y_test)
print('Model accuracy of polynomial kernal is ',accuracy_score(y_test,y_predict))

print('Using Support vector classification Method')
model = SVC(kernel='rbf',gamma=16,C=5)
model.fit(x_train,y_train)
y_predict = model.predict(x_test)
y_predict = np.round(y_predict)
y_test = np.round(y_test)
print('Model accuracy of rbf kernal is ',accuracy_score(y_test,y_predict))

model = SVC(kernel='poly',degree=5)
model.fit(x_train,y_train)
y_predict = model.predict(x_test)
y_predict = np.round(y_predict)
y_test = np.round(y_test)
print('Model accuracy of polynomial kernal is ',accuracy_score(y_test,y_predict))

print('Using decision Tree classifier')
from sklearn.tree import DecisionTreeClassifier
Model_DT = DecisionTreeClassifier()
Model_DT.fit(x_train,y_train)
y_predict = Model_DT.predict(x_test)
print('Accuracy score after using Decision Tree is:',accuracy_score(y_test,y_predict))

print('Model Optimization or Hyper parameter tuning')
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RepeatedStratifiedKFold
Model_DT = DecisionTreeClassifier()
criterion = ['gini','entropy']
splitter = ['best','random']
min_samples_split = range(1,100)
Param = dict(criterion=criterion,splitter=splitter,min_samples_split=min_samples_split)
cv = RepeatedStratifiedKFold(n_splits=5,random_state=101)
Rrid_search_cv_dt = GridSearchCV(estimator=Model_DT,param_grid=Param,scoring='accuracy',cv=cv)
Rrid_search_cv_dt.fit(x_train,y_train)
y_predict = Rrid_search_cv_dt.predict(x_test)
print('Accuracy score after GridSV is',accuracy_score(y_test,y_predict))