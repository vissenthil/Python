import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ydata_profiling import ProfileReport
data = pd.read_csv('D:\\python\\MLProjects\\MLForCloudDeployment_Heroku\\SourceFiles\\winequality-red.csv')
print(data.describe())
print('Checking Null values in the data set')
print(data.isnull().sum())
#report = ProfileReport(data,title='Profile Report for SVM')
#report.to_file('ProfileReportForSVM')
sns.scatterplot(data=data,x='density',y='pH')
plt.show()
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
new_data = scaler.fit_transform(data.drop(labels=['quality'],axis=1))
print(data.columns)
scaled_data = pd.DataFrame(new_data,columns=['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
       'pH', 'sulphates', 'alcohol'])
print('New data columns now.')
print(scaled_data.columns)
print(scaled_data.head(20))
from sklearn.preprocessing import RobustScaler
r_scalar = RobustScaler()
r_scaler_data = r_scalar.fit_transform(data.drop(labels=['quality'],axis=1))
rscaled_data_df = pd.DataFrame(r_scaler_data,columns=['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
       'pH', 'sulphates', 'alcohol'])

x = rscaled_data_df
y = data['quality']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=101)
print(y)

from sklearn.svm import SVC
SVC_Model = SVC()
SVC_Model.fit(x_train,y_train)
y_predicted = SVC_Model.predict(x_test)
from sklearn.metrics import accuracy_score
print('SVC Accuracy score is:',accuracy_score(y_test,y_predicted))
print('As checked our predicted model is quite low. We have improve the accuracy using')
print('grid serach cv approch to optimize the parameter to get best accuracy')

gridscv_Model = SVC(C=3,kernel='rbf')
gridscv_Model.fit(x_train,y_train)
y_predict = gridscv_Model.predict(x_test)
print('SVC with hiper parameter Accuracy score is:',accuracy_score(y_test,y_predict))

print('Trying with logistic Regression')
from sklearn.linear_model import LogisticRegression
LR = LogisticRegression(multi_class='ovr')
LR.fit(x_train,y_train)
lr_predict = LR.predict(x_test)
print('Logistic Regression Accuracy score is:',accuracy_score(y_test,lr_predict))

from sklearn.model_selection import GridSearchCV
#grid_param ={'C':[2,5,0,1,7,10,15,23,60,100],'gamma':[1,3,6,0.1,0.00123],'kernel':('rbf','sigmoid','linear')}
grid_param = {'C': [1], 'gamma': [1], 'kernel': ['rbf']} #this is the best param we got so using this one
grid_cv =GridSearchCV(SVC(),param_grid=grid_param,verbose=1,n_jobs=2)
grid_cv.fit(x_train,y_train)
grid_predict = grid_cv.predict(x_test)
print('Best param :',grid_cv.best_params_)
print('GSR Accuracy score is:',accuracy_score(y_test,grid_predict))

print('Support vector regression')
print(''' ''')

print(''' The fit() method helps in fitting the data into a model, 
          transform() method helps in transforming the data into a form that is more suitable for the model. 
          Fit_transform() method, on the other hand, combines the functionalities of both fit() and transform() methods in one step''')

#https://www.geeksforgeeks.org/data-analysis-with-python/?ref=shm very nice one

#EDA
#1.Anaysis
print(''' 2.Preprocessing
          1. Missing values
          2. Outlyer
          3. scaling 
          4. encoding 
          5. Feature selection
          6. Transfermation
          7. Feature merging 
          8. In balanced data''' )


