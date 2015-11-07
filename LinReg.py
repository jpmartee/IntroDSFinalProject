import pandas as pd 
import numpy as np 
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from ggplot import *
import matplotlib.pyplot as plt


# Load data
weather_data = pd.read_csv('turnstile_weather_v2.csv')

# Create dummy variables for hours and units
dummy_hours = pd.get_dummies(weather_data['hour'], prefix='hour')
dummy_units = pd.get_dummies(weather_data['UNIT'], prefix='unit')

# Choose features other than dummies
feature_cols = ['rain', 'weekday', 'meantempi']
features = weather_data[feature_cols].join(dummy_units).join(dummy_hours)

# Choose dependent variable
labels = weather_data['ENTRIESn_hourly']

# Split into training and testing data
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, random_state=26)

# Fit model to testing data
linreg = LinearRegression()
linreg.fit(features_train, labels_train)

# Test our model
pred = linreg.predict(features_test)

print '\nIntercept:', linreg.intercept_
print '\nCoefficients:'
for i in zip(feature_cols, linreg.coef_):
	print i

print "\nRegression score for training data:",
print linreg.score(features_train, labels_train)

print "\nRegression score for the testing data",
print linreg.score(features_test, labels_test)

print '\nRMSE:', np.sqrt(metrics.mean_squared_error(labels_test, pred))

weather_data['residuals'] = weather_data['ENTRIESn_hourly'] - linreg.predict(features)

residuals_hist = ggplot(weather_data, aes('residuals')) +\
				 geom_histogram(alpha=0.6, binwidth=50) +\
				 scale_x_continuous(limits=(-5000, 5000)) +\
				 theme_bw()

ggsave(filename='residuals_histogram', plot=residuals_hist.pdf)