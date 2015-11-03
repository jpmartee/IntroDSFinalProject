import pandas as pd
import numpy as np
import scipy.stats

weather_data = pd.read_csv('turnstile_weather_v2.csv')

rain = weather_data[weather_data['rain'] == 1]['ENTRIESn_hourly']
no_rain = weather_data[weather_data['rain'] == 0]['ENTRIESn_hourly']

rain_mean = np.mean(rain)
no_rain_mean = np.mean(no_rain)

mw_rain = scipy.stats.mannwhitneyu(rain, no_rain)


weekday = weather_data[weather_data['weekday'] == 1]['ENTRIESn_hourly']
non_weekday = weather_data[weather_data['weekday'] == 0]['ENTRIESn_hourly']

weekday_mean = np.mean(weekday)
non_weekday_mean = np.mean(non_weekday)

mw_weekday = scipy.stats.mannwhitneyu(weekday, non_weekday)

def getIQR(data):
	return np.percentile(data, 75) - np.percentile(data, 25)

def MannWhitney(feature):
	with_feature = weather_data[weather_data[feature] == 1]['ENTRIESn_hourly']
	without_feature = weather_data[weather_data[feature] == 0]['ENTRIESn_hourly']

	with_feature_mean = np.mean(with_feature)
	without_feature_mean = np.mean(without_feature)

	mw = scipy.stats.mannwhitneyu(with_feature, without_feature)
	print '\n---- Stats on Entries based on', feature, '----'
	print '\t\t', feature, '= 1\t\t', feature, '= 0'
	print 'Median\t\t', np.percentile(with_feature, 50), '\t\t\t', np.percentile(without_feature, 50)
	print 'IQR\t\t', getIQR(with_feature), '\t\t\t', getIQR(without_feature)

	print '\n---- Results for Mann-Whitney U Test based on', feature, '----'
	print 'Mean Hourly Entries with', feature, ':', with_feature_mean
	print 'Mean Hourly Entries without', feature, ':', without_feature_mean
	print 'U :', mw[0]
	print 'p-value :', mw[1]

MannWhitney('rain')
MannWhitney('weekday') 