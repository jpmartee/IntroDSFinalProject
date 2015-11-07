import pandas as pd 
import numpy as np
from ggplot import *

weather_data = pd.read_csv('turnstile_weather_v2.csv')

rain_histogram = ggplot(weather_data, aes(x='ENTRIESn_hourly', color='rain', fill='rain')) +\
     geom_histogram(alpha=0.6, binwidth=200) +\
     scale_x_continuous(limits = (0, 15000)) +\
     ylab('Frequency') + xlab('Hourly Entries') +\
     ggtitle('Histogram of Hourly Entries \nRain vs No Rain') +\
     theme_bw()


rain_density = ggplot(weather_data, aes(x='ENTRIESn_hourly', color='rain', fill='rain')) +\
     geom_density(alpha=0.6) +\
     scale_x_continuous(limits = (0, 15000)) +\
     ylab('Probability') + xlab('Hourly Entries') +\
     ggtitle('Density Plot of Hourly Entries \nRain vs No Rain') +\
     theme_bw()


hour_density = ggplot(weather_data, aes(x='ENTRIESn_hourly', color='hour', fill='hour')) +\
     geom_density(alpha=0.6) +\
     scale_x_continuous(limits = (0, 7500)) +\
     ylab('Probability') + xlab('Hourly Entries') +\
     ggtitle('Density Plot of Hourly Entries \nby Hour of Day') +\
     theme_bw()


weekday_density = ggplot(weather_data, aes(x='ENTRIESn_hourly', color='weekday', fill='weekday')) +\
     geom_density(alpha=0.6) +\
     scale_x_continuous(limits = (0, 15000)) +\
     ylab('Probability') + xlab('Hourly Entries') +\
     ggtitle('Density Plot of Hourly Entries \nWeekday vs Weekend') +\
     theme_bw()


ggsave(filename='rain_histogram.pdf', plot=rain_histogram)
ggsave(filename='rain_density.pdf', plot=rain_density)
ggsave(filename='hour_density.pdf', plot=hour_density)
ggsave(filename='weekday_density.pdf', plot=weekday_density)