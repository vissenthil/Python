#https://www.youtube.com/watch?v=fw5rkjq4Tfo&list=PLfFghEzKVmjvuSA67LszN1dZ-Dd_pkus6&index=3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.datasets as dataset
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics # for evaluation
print("Importing Boston House Price prediction Data Set")

House_Price_data = dataset.load_boston()
#print(House_Price_data)
df = pd.DataFrame(House_Price_data.data,columns=House_Price_data.feature_names)
df['price'] =House_Price_data.target
print(df.head(5))
print('To check number of rows and columns in our dataset')
print(df.shape)
print('To check the missing values df.isnull()')
print(df.isnull().sum())
print('Statical mesure of the data')
print(df.describe())
print('''Understanding correlation between various features in the dataset
       1. passtive correlation
       2. Negative Correlation ''')
correlation = df.corr()
print(correlation)
print('constructing headmap to understand the correlation')
plt.figure(figsize=(10,10))
sns.heatmap(correlation,cbar=True,square =True,fmt='.1f', annot=True, annot_kws={'size':8},cmap='Blues')
plt.show()
print('Now spliting data as features(indepentant) and target(depentant')
x = df.drop(['price'],axis=1) # axis =1 means droping column 0 meams droping rows
y = df['price']

print('spliting the data as train test split')
X_train,X_Test,Y_Train,Y_Test = train_test_split(x,y, test_size=0.2 ,random_state=101)

print(X_train.shape) # 80% goes to traing set
print(X_Test.shape)  # 20% goes to testing set

print('Model training now')

model = XGBRegressor()

print('Training the model with training data')
model.fit(X_train,Y_Train) # X_Train will contain features columns ,Y_Train will hold
                           # target values here price
print('Evaluation prediction on training data')
print('Accuray on predition on training data')
Training_data_prediction = model.predict(X_train)
print(Training_data_prediction)
print('R-Square error')
score_1 = metrics.r2_score(Y_Train,Training_data_prediction)
# Here Y_Train will have original price values and
# Training_data_prediction will contain the our model predicted values
print('Mean absulte error')
score_2 = metrics.mean_absolute_error(Y_Train,Training_data_prediction)
print(f'Training data R-Squared Error={score_1} and MAE = {score_2}')
print('Evaluating original varsus Predicted vlues using graph')

plt.scatter(Y_Train,Training_data_prediction)
plt.xlabel('Original Price')
plt.ylabel('Predicted price')
plt.title('Original versus Predicted price chart')
plt.show()

print('Evaluation prediction on Test data')
print('Accuray on predition on Testing data')
Testing_data_prediction = model.predict(X_Test)
print(Testing_data_prediction)
print('R-Square error')
score_1 = metrics.r2_score(Y_Test,Testing_data_prediction)
# Here Y_Test will have original price values and
# Testing_data_prediction will contain the our model predicted values
print('Mean absulte error')
score_2 = metrics.mean_absolute_error(Y_Test,Testing_data_prediction)

print(f'Testing data R-Squared Error={score_1} and MAE = {score_2}')

plt.scatter(Y_Test,Testing_data_prediction)
plt.xlabel('Original Price')
plt.ylabel('Predicted price')
plt.title('Test Original versus Predicted price chart')
plt.show()
