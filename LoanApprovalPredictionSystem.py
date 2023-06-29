#https://www.youtube.com/watch?v=x2NrPeHSPU0&t=0s
from sklearn import svm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
print('Loan approval Prediction System')
print(''' What is Seaborn?
          An open-source Python library based on matplotlib is called Seaborn. 
            It is utilized for data exploration and data visualization.
            With data frames and the Pandas library, Seaborn functions with ease''')

data = pd.read_csv('D:\\python\\MLProjects\\Loan.csv')
df = pd.DataFrame(data)
print(df.head(10))
print(df.describe())
print(df.info())
print('To findout missing values in the dataset')
print(df.isnull().sum())
df['LoanAmount_log'] = np.log(df['LoanAmount'])
print(df['LoanAmount_log'].hist(bins=20))
plt.hist(df['LoanAmount_log'],bins=20)
plt.show()
print(df.isnull().sum())
df['Totalincome'] = df['ApplicantIncome'] + df['CoapplicantIncome']
df['Totalincome_log'] =np.log(df['Totalincome'])
plt.hist(df['Totalincome_log'],bins=20)
''' plt.show()'''

print('Mode :',df['Gender'].mode()[0])
df['Gender'].fillna(df['Gender'].mode()[0],inplace=True)
df['Married'].fillna(df['Married'].mode()[0],inplace=True)
df['Dependents'].fillna(df['Dependents'].mode()[0],inplace=True)
df['Self_Employed'].fillna(df['Self_Employed'].mode()[0],inplace=True)
df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0],inplace=True)
df['Credit_History'].fillna(df['Credit_History'].mode()[0],inplace=True)
df.LoanAmount = df.LoanAmount.fillna(df.LoanAmount.mean())
df.LoanAmount_log = df.LoanAmount_log.fillna(df.LoanAmount_log.mean())
sns.countplot(x='Gender',data = df)
plt.show()
print(df.isnull().sum())
print('Number of people who takes the laon as a Gender')
print('Gender count:',df['Gender'].value_counts())

print('Number of people who takes the laon as a Married')
print('Married count:',df['Married'].value_counts())
sns.countplot(x='Married',data = df)
plt.show()

print('Number of people who takes the laon as a Dependents')
print('Dependents count:',df['Dependents'].value_counts())
sns.countplot(x='Dependents',data = df)
plt.show()


print('Number of people who takes the laon as a Self_Employed')
print('Self_Employed count:',df['Self_Employed'].value_counts())
sns.countplot(x='Self_Employed',data = df)
plt.show()

x = df.iloc[:,np.r_[1:5,9:11,13:15]].values
y = df.iloc[:,12].values

print(x)
from sklearn.model_selection import train_test_split
X_Train,X_Test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.preprocessing import LabelEncoder
LabelEncoder_x = LabelEncoder()
for i in range(0,5):
    X_Train[:,i] = LabelEncoder_x.fit_transform(X_Train[:,i])
    X_Train[:,7] = LabelEncoder_x.fit_transform(X_Train[:,7])

LabelEncoder_y = LabelEncoder()

y_train = LabelEncoder_y.fit_transform(y_train)

print('For Test Data Set')
for i in range(0,5):
    X_Test[:,i] = LabelEncoder_x.fit_transform(X_Test[:,i])
    X_Test[:,7] = LabelEncoder_x.fit_transform(X_Test[:,7])

LabelEncoder_y = LabelEncoder()

y_test = LabelEncoder_y.fit_transform(y_test)

from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
X_Train = ss.fit_transform(X_Train)
X_Test  = ss.fit_transform(X_Test)

from sklearn.ensemble import RandomForestClassifier
rf_clf = RandomForestClassifier()
rf_clf.fit(X_Train,y_train)

from sklearn import metrics
y_predict = rf_clf.predict(X_Test)

print('Metrics of randomForest accurecy is',metrics.accuracy_score(y_predict,y_test))

from sklearn.naive_bayes import GaussianNB
nb_clf = GaussianNB()
nb_clf.fit(X_Train,y_train)
nb_predict = nb_clf.predict(X_Test)

print('Metrics of GaussianNB accurecy is',metrics.accuracy_score(nb_predict,y_test))

from sklearn.tree import DecisionTreeClassifier
dt_clf = DecisionTreeClassifier()
dt_clf.fit(X_Train,y_train)
dt_predict = dt_clf.predict(X_Test)

print('Metrics of DecisionTreeClassifier accurecy is',metrics.accuracy_score(dt_predict,y_test))


from sklearn.neighbors import KNeighborsClassifier
kn_clf = KNeighborsClassifier()
kn_clf.fit(X_Train,y_train)
kn_predict = kn_clf.predict(X_Test)

print('Metrics of KNeighborsClassifier accurecy is',metrics.accuracy_score(kn_predict,y_test))

