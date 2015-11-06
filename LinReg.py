import pandas as pd 
import numpy as np 
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics

weather_data = pd.read_csv('turnstile_weather_v2.csv')
dummy_hours = pd.get_dummies(weather_data['hour'], prefix='hour')
dummy_units = pd.get_dummies(weather_data['UNIT'], prefix='unit')

feature_cols = ['rain', 'fog', 'weekday']
features = weather_data[feature_cols].join(dummy_units).join(dummy_hours)

labels = weather_data['ENTRIESn_hourly']

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, random_state=26)

linreg = LinearRegression()
linreg.fit(features_train, labels_train)

pred = linreg.predict(features_test)

print np.sqrt(metrics.mean_squared_error(labels_test, pred))
print linreg.score(features, labels)