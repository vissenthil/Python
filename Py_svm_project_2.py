import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv('D:\\python\\MLProjects\\MLForCloudDeployment_Heroku\\SourceFiles\\cell_samples.csv')
print(data.describe())
print(data.columns)
print(data.isnull().sum())
print(data['Class'])
print('Distribution of classes')
bengin_data = data[data['Class'] == 2][0:200] # Filtering Only 200 records
malignant_data = data[data['Class'] == 4][0:200] # Filtering Only 200 records
print(bengin_data.head(10))
#print(help(bengin_data.plot()))
bengin_data.plot(kind='scatter',x='Clump',y='UnifSize',color='blue',label='bengin')
malignant_data.plot(kind='scatter',x='Clump',y='UnifSize',color='red',label='malignant')
plt.show()

axes = bengin_data.plot(kind='scatter',x='Clump',y='UnifSize',color='blue',label='bengin')
malignant_data.plot(kind='scatter',x='Clump',y='UnifSize',color='red',label='malignant',ax=axes)
plt.show()
print(data.dtypes)
print('BareNuc Column is non inter column need to change to numeric')
data = data[pd.to_numeric(data['BareNuc'],errors='coerce').notnull()]
data['BareNuc'] = data['BareNuc'].astype('int')
print(data.dtypes)
print('Removind unwanted columns')
fetaure_data = data.drop(['ID','Class'],axis=1)
print(fetaure_data)
target_data = data['Class']
print('Target data')
print(target_data)
x = fetaure_data
y = target_data
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
X_train,X_Test, y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=144)
Model = SVC(kernel='poly',degree=4)
Model.fit(X_train,y_train)
y_predict = Model.predict(X_Test)
from sklearn.metrics import accuracy_score
print('Accuracy of the over model is ',accuracy_score(y_test,y_predict))
print('SVM Using linear kernel')
Model = SVC(kernel='linear',gamma='auto',C=5)
Model.fit(X_train,y_train)
y_predict = Model.predict(X_Test)
from sklearn.metrics import accuracy_score
print('Accuracy of the over model with linear is ',accuracy_score(y_test,y_predict))

print('SVM Using linear rbf Radial basis function')
Model = SVC(kernel='rbf',gamma='scale',C=5)
Model.fit(X_train,y_train)
y_predict = Model.predict(X_Test)
from sklearn.metrics import accuracy_score
print('Accuracy of the over model with rbf is ',accuracy_score(y_test,y_predict))


print('SVM Using linear sigmoid function')
Model = SVC(kernel='sigmoid',gamma='scale',C=5)
Model.fit(X_train,y_train)
y_predict = Model.predict(X_Test)
from sklearn.metrics import accuracy_score
print('Accuracy of the over model with sigmoid is ',accuracy_score(y_test,y_predict))