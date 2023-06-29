import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model  import Ridge,Lasso,RidgeCV, LassoCV, ElasticNet, ElasticNetCV, LogisticRegression
from sklearn.model_selection import train_test_split
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.metrics import accuracy_score, confusion_matrix, roc_curve, roc_auc_score
import matplotlib.pyplot as plt
#from pandas_profiling import ProfileReport
from ydata_profiling import ProfileReport

import seaborn as sns
import pickle
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv")
print(df.head(25))
print(df.isnull().sum())
print('1. Collect the data')
print('2. EDA')
#Report = ProfileReport(df)
#Report.to_file('Report.html')
df['BMI'] = df['BMI'].replace(0,df['BMI'].mean())
print('Just replacing columns having zero values with mean values')
columns = ''
count = 0

for columns_list in df.columns :
   # checking if the datatype is int or float only we want to replace woith mean values
   if df[columns_list].dtype == 'int64' or df[columns_list].dtype == 'float64' :
        columns = df[columns_list]
        count = (columns == 0).sum()
        if count !=0 :
            df[columns_list] = df[columns_list].replace(0,df[columns_list].mean())

#Report = ProfileReport(df)
#Report.to_file('Report.html')
fig,ax = plt.subplots(figsize=(20,10))
sns.boxplot(data= df, ax=ax)
plt.show()

# Here 70 only we are going to have in Insulin field others are outlayers so excluding that data

q = df['Pregnancies'].quantile(.98)
df_new = df[df['Pregnancies'] < q]

q = df_new['BMI'].quantile(.99)
df_new = df_new[df_new['BMI']< q]

q = df_new['SkinThickness'].quantile(.99)
df_new = df_new[df_new['SkinThickness']< q]

q = df_new['Insulin'].quantile(.95)
df_new = df_new[df_new['Insulin']< q]

q = df_new['DiabetesPedigreeFunction'].quantile(.99)
df_new = df_new[df_new['DiabetesPedigreeFunction']< q]


q = df_new['Age'].quantile(.99)
df_new = df_new[df_new['Age']< q]


def Out_layerRemoval(self,data):
    def out_layer_limit(col):
        Q3,Q1 = np.nanpercentile(col,[75,25])
        IQR = Q3 - Q1
        UL = Q3 + 1.5 * IQR
        LL = Q1 - 1.5 * IQR
        return UL,LL
    for column in df.columns :
        if df[column].dtype == 'int64':
            UL,LL = out_layer_limit(column)
            df[column] = np.where((df[column] > UL | df[column] < ll),np.nan,df[column])
        return data



fig ,ax  = plt.subplots(figsize = (20,20))
sns.boxplot(data = df_new , ax = ax)
plt.show()

Out_layerRemoval(df,df)

print('Checking outlayer after excluding Data using IQR Methods')
fig,ax = plt.subplots(figsize=(20,10))
sns.boxplot(data= df, ax=ax)
plt.show()

X = df_new.drop(columns=['Outcome'])
y = df_new['Outcome']
scalar = StandardScaler()
ProfileReport(pd.DataFrame(scalar.fit_transform(X)))
X_scaled = scalar.fit_transform(X)
#X_scaled = np.round(X_scaled)
y = np.round(y)
df_new_scalar = pd.DataFrame(scalar.fit_transform(df_new))
fig ,ax  = plt.subplots(figsize = (20,20))
sns.boxplot(data = df_new_scalar , ax = ax)
plt.show()
def vif_score(x):
    scaler = StandardScaler()
    arr = scaler.fit_transform(x)
    return pd.DataFrame([[x.columns[i], variance_inflation_factor(arr,i)] for i in range(arr.shape[1])], columns=["FEATURE", "VIF_SCORE"])

vif_score(X)

x_train, x_test, y_train, y_test = train_test_split(X_scaled , y , test_size = .20 , random_state = 144)

print('y Value is',y)

log_reg = LogisticRegression(verbose=1)
log_reg.fit(x_train,y_train )
prob = log_reg.predict_proba([x_test[2]])
print(f'Probability is :{prob}')
print('Predict the value for one recrod :')
print(log_reg.predict([x_test[2]]))
print('Bulk Prediction ')
y_predict = log_reg.predict(x_test)

print('Predicted values are :',y_predict)
print('Actul values of dependant variable is:',np.array(y_test))

from sklearn.metrics import confusion_matrix,accuracy_score,classification_report,roc_curve

con_matrix = confusion_matrix(y_test,y_predict)
print(con_matrix)

true_negative = con_matrix[0][0]
false_pastive = con_matrix[0][1]
false_negative = con_matrix[1][0]
true_pastive  = con_matrix[1][1]
#Precision
Precision = (true_pastive) / (true_pastive + false_pastive)
print('Precision value is ',Precision)

#Recall
Recall = (true_pastive) / (true_pastive + false_negative)
print('Recall value is',Recall)
#f1 Score
F1_Score = 2 * (Recall * Precision) / ( Recall + Precision)
print('F1 Score value is',F1_Score)
#Area under curve
AUC = roc_auc_score(y_test,y_predict)
print('AUC Is :',AUC)
clf_rep = classification_report(y_test,y_predict)
print('Classification Report is:')
print(clf_rep)

def Model_eval(y_treu,y_predict) :
    tn,fp,fn,tp = confusion_matrix(y_test,y_predict).ravel()
    accuray = (tp + fn) / (tp + tn + fn + tp )
    precision = tp / (tp + fp)
    recall = tp / ( tp + fn)
    specificity = tn / (fp + tn)
    F1_Score = 2 * (Recall * Precision) / (Recall + Precision)
    result = {'Accuray':accuray,'precision':precision,'recall':recall,
              'spcificity':specificity,'F1_Score':F1_Score}
    return result
eval_result = Model_eval(y_test,y_predict)
print('Evaluvation Results')
print(eval_result)
prob = log_reg.predict_proba(x_test)
prob = prob[:,1]
fpr,tpr, thresholds = roc_curve(y_test,prob)
print('FPR is',fpr)
print('Thresholds value is:',thresholds)

plt.plot(fpr,tpr,color='Orange',label='ROC')
plt.plot([0,1],[0,1],color ='darkblue',linestyle='--',label ='ROC Curve (area %0.2f)' %AUC)
plt.xlabel('False pastive rate')
plt.ylabel('True pastive Rate')
plt.title('Reciever Opearting Characterstic (ROC) Curve')
plt.legend()
plt.show()


#Breaking down the accuracy score formula

Accuracy = (true_pastive + true_negative) / (true_pastive + false_pastive + false_pastive + false_negative)
print('Manuvally calculated accuracy is:',np.round(Accuracy))
acc = accuracy_score(y_test,y_predict)
print('Accuracy score is :',np.round(acc))

print('Hyper parameter tuning')
print('Hyper param are in lg is:')
print(log_reg.get_params())
print('Getting param keys')
print(log_reg.get_params().keys())
param_grid = { 'penalty':['l1','l2','elasticnet'],
               'C':np.logspace(-4,4,20),
                'solver':['liblinear','lbfgs','sag','saga']
                }
from sklearn.model_selection import GridSearchCV,RandomizedSearchCV
log_reg_gscv = GridSearchCV(estimator=log_reg,param_grid=param_grid,cv=5)

log_reg_gscv.fit(x_train,y_train)
print('Getting best parameter')
print(log_reg_gscv.best_params_)
print('Now creating new model with this best parameter will imporve the accuracy')
log_reg = LogisticRegression(C=0.23357214690901212, penalty =  'l1', solver = 'liblinear')
log_reg.fit(x_train,y_train)
y_predict = log_reg.predict(x_test)
accuracy = accuracy_score(y_test,y_predict)
print('Now accuracy is:',accuracy)
print('Using RandomizedSearchCV Model')
import warnings
warnings.filterwarnings('ignore')
log_reg_rscv = RandomizedSearchCV(estimator=log_reg,param_distributions=param_grid)
log_reg_rscv.fit(x_train,y_train)
print('Best parameter for RandomizedSeachCV Is:')
print(log_reg_rscv.best_params_)

log_reg = LogisticRegression(solver='saga', penalty= 'l1', C=1.623776739188721)
log_reg.fit(x_train,y_train)
y_predict = log_reg.predict(x_test)
acc = accuracy_score(y_test,y_predict)
print('Accuracy score in RamdomizedSearchCV is :',acc)
