# Support vector classification - Algorithm.(SVM)
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
import numpy as np
# importing the dataset
data = pd.read_csv('D:\\python\\MLProjects\\MLForCloudDeployment_Heroku\\SourceFiles\\Social_Network_ads.csv')
print(data.describe())

x = data.iloc[:,[2,3]]
y = data.iloc[:,4]

# Splitting data into training and test set
from sklearn.model_selection import train_test_split
X_train,X_Test,y_train,y_test = train_test_split(x,y,test_size=0.3, random_state=144)
# Features scaling
from sklearn.preprocessing import StandardScaler
scalar = StandardScaler()
x_train = scalar.fit_transform(X_train)
X_Test  = scalar.fit_transform(X_Test)
# Applying SVM

from sklearn.svm import SVC
Classifier = SVC(kernel='linear',random_state=0)
Classifier.fit(x_train,y_train)
y_predict = Classifier.predict(X_Test)
print('Accuracy score of svm of linear kernal is:',accuracy_score(y_test,y_predict))

print('Kernal rbf with default parameter')
from sklearn.svm import SVC
Classifier = SVC(kernel='rbf',random_state=0)
Classifier.fit(x_train,y_train)
y_predict = Classifier.predict(X_Test)
print('Accuracy score of svm of rbf kernal is:',accuracy_score(y_test,y_predict))

print('Kernal rbf with hiper parameter')
from sklearn.svm import SVC
Classifier = SVC(kernel='rbf',gamma=13,C=1,random_state=0)
Classifier.fit(x_train,y_train)
y_predict = Classifier.predict(X_Test)
print('Accuracy score of svm of rbf Hiper param kernal is:',accuracy_score(y_test,y_predict))


print('using Kernal as Polynomiyal ')
from sklearn.svm import SVC
Classifier = SVC(kernel='poly',degree=4)
Classifier.fit(x_train,y_train)
y_predict = Classifier.predict(X_Test)
print('Accuracy score of svm of polynomiyal kernal is:',accuracy_score(y_test,y_predict))
