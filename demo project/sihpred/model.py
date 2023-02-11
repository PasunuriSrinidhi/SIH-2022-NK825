import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
import pickle
import seaborn as sns
from sklearn.linear_model import LinearRegression, RidgeCV, LassoCV, ElasticNetCV
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn import linear_model
df = pd.read_csv('longitude.csv')
df1 = pd.read_csv('latitude.csv')

df1.isnull().sum().sort_values(ascending=False)
df_no_missing = df1.dropna(axis=0)

df.isnull().sum().sort_values(ascending=False)
df_no_missing = df.dropna(axis=0)


from sklearn import svm

regr = svm.SVR()

from sklearn import metrics

X = df[['sst', 'atms', 'u10', 'v10']]

Y = df[['delta_longi']]
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=1 / 4, random_state=0)

# with sklearn
regr1 = svm.SVR()
regr1.fit(X_train, Y_train)
pickle.dump(regr1, open('m1.pkl', 'wb'))
# regr1.save('m1.pkl')
Y_pred=regr1.predict([[-78.07,54.293,-0.75,-1]])

# Predicting the Test set results
# Y_pred = regr1.predict(X_test)
# for i in Y_pred:
#     # print(i)
#     pass

# print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(Y_test, Y_pred)))

from sklearn import metrics

X = df1[['sst', 'atms', 'u10', 'v10']]

Y = df1[['delta_lati']]
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=1 / 4, random_state=0)

# with sklearn

regr = svm.SVR()
regr.fit(X_train, Y_train)
pickle.dump(regr, open('m2.pkl', 'wb'))#latitude
# Predicting the Test set results
# Y_pred = regr.predict(X_test)
# for i in Y_pred:
#     # print(i)
#     pass
#
# print('Root Mean Squared Error1:', np.sqrt(metrics.mean_squared_error(Y_test, Y_pred)))

